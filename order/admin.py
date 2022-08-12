from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'created', 'status']
    list_filter = ['status']
    
admin.site.register(Order, OrderAdmin)
