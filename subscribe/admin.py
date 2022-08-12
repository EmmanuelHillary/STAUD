from django.contrib import admin
from .models import Subscribe, Newsletter

class SubscribeAdmin(admin.ModelAdmin):
    list_display = ['email']

admin.site.register(Subscribe, SubscribeAdmin)
admin.site.register(Newsletter)
