from rest_framework import serializers
from .models import Company
from accounts.serializers import AgentSerializer
from accommodation.serializers import AccommodationAPISerializer
from accommodation.models import AccommodationInfo
from accommodation.serializers import (CAMPUS, ACCOMMODATION_TYPE, FURNISHED, PRICE, ROOM_SIZE)


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            "id",
            "name",
            "display_picture",
            "description",
            "address",
            "mobile_number",
            "telephone_number",
            "email",
        ]

class CompanyDetailSerializer(serializers.ModelSerializer):
    socials = serializers.SerializerMethodField(read_only=True)
    featured_agents = serializers.SerializerMethodField(read_only=True)
    staud_listings = serializers.SerializerMethodField(read_only=True)
    accommodation_type = serializers.SerializerMethodField(read_only=True)
    campus = serializers.SerializerMethodField(read_only=True)
    price = serializers.SerializerMethodField(read_only=True)
    room_size = serializers.SerializerMethodField(read_only=True)
    furnished = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Company
        fields = [
            "name",
            "display_picture",
            "description",
            "address",
            "mobile_number",
            "telephone_number",
            "email",
            "socials",
            "featured_agents",
            "staud_listings",
            "accommodation_type",
            "campus",
            "price",
            "room_size",
            "furnished"
        ] 
    def get_socials(self, obj):
        data = [{social.social_name :social.social_handle} for social in obj.company_socials.all()]
        return data
    
    def get_featured_agents(self, obj):
        qs = obj.company_agent.all().order_by("-staud_rating")[:3]
        data = AgentSerializer(qs, many=True).data
        return data
    
    def get_staud_listings(self, obj):
        objc = AccommodationInfo.objects.filter(company=obj)
        qs = []
        for acc in objc:
            qs += acc.accommodation_info.all().order_by("-updated")
        qs = sorted(qs , key = lambda x: x.updated).__reversed__()
        data = AccommodationAPISerializer(qs, many=True).data
        return data

    def get_accommodation_type(self, obj):
        return ACCOMMODATION_TYPE
    
    def get_campus(self, obj):
        return CAMPUS
    
    def get_price(self, obj):
        return PRICE
    
    def get_room_size(self, obj):
        return ROOM_SIZE
    
    def get_furnished(self, obj):
        return FURNISHED


