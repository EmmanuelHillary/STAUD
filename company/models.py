from django.db import models
from django.template.defaultfilters import slugify
from django.db.models import Q


def get_upload_path(instance, filename):
    model = instance.name
    name = model.replace(' ', '_')
    return f'{name}/images/{filename}'

class Company(models.Model):
    name = models.CharField(max_length=130, unique=True)
    slug = models.SlugField(null=False, unique=True)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    mobile_number = models.CharField(max_length=20, null=True, blank=True)
    telephone_number = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    display_picture = models.ImageField(default='company.jpg', upload_to=get_upload_path)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_featured_agents(self):
        company = Company.objects.filter(name=self.name)
        for cm in company:
            agents = cm.company_agent.all().filter(staud_rating__gte=4).order_by('-number_of_sales_made')
        return agents
    
    def get_staud_listings(self):
        staud_listing = []
        company = Company.objects.filter(name=self.name)
        for cm in company:
            lists = cm.company_accommodation.all()
        for L in lists:
            staud_listing += L.accommodation_info.all()
        return staud_listing
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'Companies'

class CMSocialMedia(models.Model):
    conpany = models.ForeignKey(Company, related_name="company_socials", on_delete=models.CASCADE)
    social_name = models.CharField(max_length=250, blank=True, null=True)
    social_handle = models.CharField(max_length=250, blank=True, null=True)
    
