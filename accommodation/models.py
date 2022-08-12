from django.db import models
from accounts.models import Agent
from company.models import Company
from django.utils import timezone

ACCOMMODATION_TYPE = (
    ('Apartment', 'Apartment'),
    ('Hostel', 'Hostel'),
)    


ROOM_SIZE = (
    ('One man room', 'One man room'),
    ('Two man room', 'Two man room'),
    ('Three man room', 'Three man room'),
    ('Four man room', 'Four man room'),
    ('Six man room', 'Six man room'),
    ('Eight man room', 'Eight man room'),
    ('Ten man room', 'Ten man room'),
    ('Miniflat', 'Miniflat'),
    ('Self contain', 'Self contain'),
)

SEX = (
    ('Female', 'Female'),
    ('Male', 'Male'),
    ('Unisex', 'Unisex'),
)

FURNISHED = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)

MARKET_STATUS = (
    ('Available', 'Available'),
    ('Unavailable', 'Unavailable'),
)

class Campus(models.Model):
    name = models.CharField(max_length=130)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Campus"

class Location(models.Model):
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class AccommodationInfo(models.Model):
    name = models.CharField(max_length=130, unique=True)
    number_of_sales = models.PositiveIntegerField(default=0)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_accommodation', blank=True, null=True)
    total_amount_sold = models.PositiveIntegerField(default=0)
    short_description = models.TextField()
    registration_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Accommodation Info"

class Image(models.Model):
    accomodation = models.ForeignKey(AccommodationInfo, on_delete=models.CASCADE) 
    images = models.ImageField(null=True, blank=True, default='accommodation.png')

class AccommodationManager(models.Manager):
    def get_all_apartments(self):
        return Accommodation.objects.all().filter(accommodation_type='Apartment')
    def get_all_hostels(self):
        return Accommodation.objects.all().filter(accommodation_type='Hostel')
    def get_featured_staud(self):
        return Accommodation.objects.all().order_by('-units_sold')

def get_upload_path_acc(instance, filename):
    model = instance.accommodation.name
    acc_type = instance.accommodation_type
    name = model.replace(' ', '_')
    return f'{name}/images/{acc_type}/{filename}'

class Accommodation(models.Model):
    accommodation = models.ForeignKey(AccommodationInfo, on_delete=models.CASCADE, related_name='accommodation_info')
    accommodation_type = models.CharField(choices=ACCOMMODATION_TYPE, max_length=10)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, related_name="campus")
    address = models.CharField(max_length=250)
    sex = models.CharField(choices=SEX, max_length=10, default='none')
    price = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True, blank=True)
    room_size = models.CharField(choices=ROOM_SIZE, max_length=25)
    furnished = models.CharField(choices=FURNISHED, max_length=5)
    full_description = models.TextField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    market_status = models.CharField(choices=MARKET_STATUS, max_length=15)
    staud_id = models.CharField(max_length=12)
    units_sold = models.PositiveIntegerField(null=True, blank=True, default=0)
    number_of_views = models.PositiveIntegerField(null=True, blank=True, default=0)
    display_picture = models.ImageField(default='accommodation.PNG', upload_to=get_upload_path_acc)

    objects = AccommodationManager()

    def __str__(self):
        return self.accommodation.name + ' (' + self.accommodation_type + ') '
    
    def room_sizes(self):
        return self.get_room_size_display()
    
    class Meta:
        ordering = ['-updated']

def get_upload_path(instance, filename):
    model = instance.accommodation.accommodation.name
    acc_type = instance.accommodation.accommodation_type
    name = model.replace(' ', '_')
    return f'{name}/images/{acc_type}/{filename}'

class AccommodationImage(models.Model):
    accommodation = models.ForeignKey(Accommodation, related_name="accommodation_images", on_delete=models.CASCADE) 
    images = models.ImageField(null=True, blank=True, upload_to=get_upload_path, default='accommodation.png')
    
    def __str__(self):
        return self.accommodation.accommodation.name

class TopFeature(models.Model):
    accommodation = models.ForeignKey(Accommodation, related_name="accommodation_top_features", on_delete=models.CASCADE)
    feature = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.accommodation.accommodation.name

    