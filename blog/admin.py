from django.contrib import admin
from .models import Post, Comments, PostLikes
from mptt.admin import MPTTModelAdmin

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'blogger', 'status', 'created']
    list_filter = ['status', 'updated', 'created']
    search_fields = ('title', 'blogger__user__username')
    list_editable = ['status']
    date_hierarchy = 'created'

admin.site.register(Post, PostAdmin)
admin.site.register(PostLikes)
admin.site.register(Comments, MPTTModelAdmin)
