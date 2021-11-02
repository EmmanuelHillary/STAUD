from django.contrib import admin
from .models import Subscribe, Newsletter

class SubscribeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'date_added']

admin.site.register(Subscribe, SubscribeAdmin)
admin.site.register(Newsletter)
