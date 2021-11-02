from django.db import models



class Subscribe(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
    class Meta:
        ordering = ['email']
        verbose_name_plural = 'Subscribers'

class Newsletter(models.Model):
    EMAIL_STATUS_CHOICES = (
        ('Draft', 'Draft'),
        ('Published', 'Published')
    )
    subject = models.CharField(max_length=250)
    body = models.TextField(null=True, blank=True)
    email = models.ManyToManyField(Subscribe)
    status = models.CharField(choices=EMAIL_STATUS_CHOICES, default='Draft', max_length=13)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject
    
    class Meta:
        ordering = ['-updated']
    
    