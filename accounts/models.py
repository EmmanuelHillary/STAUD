from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from company.models import Company

class Blogger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    email = models.EmailField()
    email_confirmed = models.BooleanField(default=False)
    campus = models.CharField(max_length=250, null=True, blank=True)
    phone_number = models.CharField(max_length=250)
    bio = models.TextField()
    display_picture = models.ImageField(default='avatar.png', upload_to='blog/profile/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

class Agent(models.Model):
    first_name = models.CharField(max_length=130)
    last_name = models.CharField(max_length=130)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=250)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    mobile_number = models.CharField(max_length=20, null=True, blank=True)
    whatsapp_number = models.CharField(max_length=20, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_agent', default='None', blank=True, null=True)
    staud_rating = models.DecimalField(decimal_places=1, default=0, max_digits=4)
    number_of_sales_made = models.PositiveIntegerField(default=0, null=True, blank=True)
    display_picture = models.ImageField(default='avatar.png', upload_to='agent/profile/')
    review = models.CharField(max_length=250, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.first_name + ' ' + self.last_name) 
    



