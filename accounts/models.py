from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from company.models import Company

ACCOUNT_TYPE = (
    ('Estate Agent', 'es'),
    ('Property Developer', 'pd'),
    ('Property Owner', 'po'),
)

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
    username = models.CharField(max_length=130, default="None")
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=250)
    account_type = models.CharField(choices=ACCOUNT_TYPE, max_length=25, null=True, blank=True)
    mobile_number = models.CharField(max_length=20, null=True, blank=True)
    whatsapp_number = models.CharField(max_length=20, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_agent', blank=True, null=True)
    staud_rating = models.DecimalField(decimal_places=1, default=0, max_digits=4)
    number_of_sales_made = models.PositiveIntegerField(default=0, null=True, blank=True)
    display_picture = models.ImageField(default='avatar.png', upload_to='agent/profile/')
    review = models.CharField(max_length=250, null=True, blank=True)
    conf_num = models.CharField(max_length=15, null=True, blank=True)
    email_verification = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.first_name + ' ' + self.last_name)



        
    



