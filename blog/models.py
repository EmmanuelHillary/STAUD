from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from accounts.models import Blogger
from .utils import time_since
from hitcount.models import HitCountMixin, HitCount
from django.utils.safestring import mark_safe
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey
import datetime
from markdown_deux import markdown
from django.utils.safestring import mark_safe
from django.db.models import Count, Sum

class PostCategories(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name
    
class PostLikes(models.Model):
    ip = models.GenericIPAddressField(default="0")
    post = models.ForeignKey('Post', related_name='likes', on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '{0} in {1} post'.format(self.ip,self.post.title)
    
    class Meta:
        verbose_name_plural = 'PostViews'

class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(PostManager, self).filter(accept=True, status='Publish').filter(publish__lte=timezone.now())
    
    def trending(self, *args, **kwargs):
        month_ago = datetime.date.today() - datetime.timedelta(weeks=4)
        trend = super(PostManager, self).filter(created__gte=month_ago)
        top_trend = sorted(trend, key=lambda t: t.trend, reverse=True)[0:3]
        return top_trend
    
    def latest_posts(self, *args, **kwargs):
        week_ago = datetime.date.today() - datetime.timedelta(days=7)
        return super(PostManager, self).filter(created__gte=week_ago)
    
    def campus_news(self, *args, **kwargs):
        return super(PostManager, self).filter(category='CAMPUS NEWS')
    
    def staud_gists(self, *args, **kwargs):
        return super(PostManager, self).filter(category='STAUD GISTS')

class Post(models.Model, HitCountMixin):
    STATUS_CHOICES = (
        ('Draft', 'Draft'),
        ('Publish', 'Publish')
    )
    CATEGORIES  = (
        ('CAMPUS NEWS', 'CAMPUS NEWS'),
        ('STAUD GISTS', 'STAUD GISTS'),
        ('REAL ESTATE INFO', 'REAL ESTATE INFO'),
        ('STAUD ADVICE', 'STAUD ADVICE')
    )
    blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)
    reject = models.BooleanField(default=False)
    accept = models.BooleanField(default=False)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    category = models.CharField(max_length=17, choices=CATEGORIES, default="CAMPUS NEWS")
    status = models.CharField(max_length=13, choices=STATUS_CHOICES, default="Draft")
    publish = models.DateField(auto_now_add=False, auto_now=False, default=timezone.now)
    thumbnail = models.FileField(blank=True, null=True, upload_to='blog/files/', default='blog.png')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    objects = PostManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})
    
    def get_markdown(self):
        content = self.content
        markdown_text = markdown(content)
        return mark_safe(markdown_text)


    class Meta:
        ordering = ['-updated']

    @property
    def trend(self):
        instance = self
        if Comments.objects.filter(post=instance):
            total_comments = Comments.objects.filter(post=instance).count()
        else:
            total_comments = 0
        if PostLikes.objects.filter(post=instance):
            total_likes = PostLikes.objects.filter(post=instance).count()
        else:
            total_likes = 0
        total_hits = instance.hit_count.hits 
        total = total_likes + total_comments + total_hits 
        return total

    @property
    def comment(self):
        instance = self
        qs = Comments.objects.filter(post=instance, parent=None).count()
        return qs

class Comments(MPTTModel):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=True, blank=True)
    parent = TreeForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    like = models.IntegerField(default=0)
    unlike = models.IntegerField(default=0)
    content = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return f'Comment by {self.name}'


    def likes(self):
        return self.like.count()

    def unlikes(self):
        return self.unlike.count()

    def children(self):  # replies
        return Comments.objects.filter(parent=self)

    class MPTTMeta:
        order_insertion_by = ['-timestamp']
    
    class Meta:
        verbose_name_plural = 'Comments'

    def time(self):
        return time_since(self.timestamp)




def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = f'{slug}{qs.first().id}'
        return create_slug(instance, new_slug=new_slug)
    return slug



def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(receiver=pre_save_post_receiver, sender=Post)
