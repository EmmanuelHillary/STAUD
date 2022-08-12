from django.contrib import admin
from .models import Company, CMSocialMedia

class CMSocialMediaAdmin(admin.StackedInline):
    model = CMSocialMedia

class CompanyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [CMSocialMediaAdmin]

@admin.register(CMSocialMedia)
class CMSocialMediaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Company, CompanyAdmin)
