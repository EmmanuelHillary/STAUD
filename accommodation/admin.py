from django.contrib import admin
from .models import Campus, Accommodation, AccommodationInfo, Location, AccommodationImage, TopFeature

class AccommodationImageAdmin(admin.StackedInline):
    model = AccommodationImage

class TopFeatureAdmin(admin.StackedInline):
    model = TopFeature

class AccommodationAdmin(admin.ModelAdmin):
    list_display = ['accommodation', 'accommodation_type', 'price', 'campus', 'market_status', 'number_of_views', 'created']
    list_filter = ['accommodation','accommodation_type', 'market_status', 'created']
    search_fields = ('accommodation', 'campus',)
    list_editable = ['market_status']
    date_hierarchy = 'created'
    inlines = [AccommodationImageAdmin, TopFeatureAdmin]

    class Meta:
        model = Accommodation

@admin.register(AccommodationImage)
class AccommodationImageAdmin(admin.ModelAdmin):
    pass

@admin.register(TopFeature)
class TopFeatureAdmin(admin.ModelAdmin):
    pass

admin.site.register(Accommodation, AccommodationAdmin)
admin.site.register(AccommodationInfo)
admin.site.register(Campus)
admin.site.register(Location)
