from django.db import models
from django.db.models.fields import TextField

STATUS = (
    ('Completed', 'Completed'),
    ('Pending', 'Pending'),
)
class OrderManager(models.Manager):
    def pending(self):
        return Order.objects.filter(status='Pending')
    def completed(self):
        return Order.objects.filter(status='Completed')
class Order(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=254, blank=True, null=True,)
    budget = models.CharField(max_length=256, blank=True, null=True)
    phone_number = models.CharField(max_length=256, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    occupation = models.CharField(max_length=256)
    accommodation_type = models.CharField(max_length=256)
    campus = models.CharField(max_length=256)
    agency = models.CharField(max_length=256)
    room_size = models.CharField(max_length=256)
    furnished = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=254, choices=STATUS, default='Pending')

    objects = OrderManager()


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']
