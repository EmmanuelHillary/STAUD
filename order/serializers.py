from rest_framework import serializers
from .models import Order
from .mail import order_email_to_staud
from accommodation.models import Campus, Location
from accommodation.serializers import (CAMPUS, ACCOMMODATION_TYPE, FURNISHED, ROOM_SIZE)
from company.models import Company
import re

AGENCY = ["Any Agency"] + [str(agency) for agency in Company.objects.all()] + ["None"] 

class OrderInlineSerializer(serializers.ModelSerializer):

    accommodation_type = serializers.SerializerMethodField(read_only=True)
    campus = serializers.SerializerMethodField(read_only=True)
    agency = serializers.SerializerMethodField(read_only=True)
    room_size = serializers.SerializerMethodField(read_only=True)
    furnished = serializers.SerializerMethodField(read_only=True)
    location = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Order
        fields = [
            "accommodation_type",
            "campus",
            "agency",
            "room_size",
            "furnished",
            "location"
        ]
    
    def get_accommodation_type(self, obj):
        return ACCOMMODATION_TYPE

    def get_campus(self, obj):
        return CAMPUS

    def get_agency(self, obj):
        return AGENCY

    def get_room_size(self, obj):
        return ROOM_SIZE

    def get_furnished(self, obj):
        return FURNISHED

    def get_location(self, obj):
        campus = [str(campus) for campus in Campus.objects.all()]
        data = {}
        for i in campus:
            data[i] = [location.name for location in Location.objects.all().filter(campus__name=i)] 
        return data

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "name",
            "email",
            "budget",
            "phone_number",
            "comment",
            "occupation",
            "accommodation_type",
            "campus",
            "agency",
            "room_size",
            "furnished",
            "location"
        ]

    def create(self, validated_data):
        name=validated_data.get('name')
        email=validated_data.get('email')
        budget=validated_data.get('budget')
        phone_number=validated_data.get('phone_number')
        comment=validated_data.get('comment') 
        occupation=validated_data.get('occupation')
        accommodation_type=validated_data.get('accommodation_type')
        campus=validated_data.get('campus')
        agency=validated_data.get('agency')  
        room_size=validated_data.get('room_size')
        furnished=validated_data.get('furnished')
        location=validated_data.get('location')
        # Send mail
        order_email_to_staud(name, budget, phone_number, occupation, email, accommodation_type, campus,
        location, agency, room_size, furnished, comment)
        order = Order.objects.create(
            name=name,
            email=email,
            budget=budget,
            phone_number=phone_number,
            comment=comment,
            occupation=occupation,
            accommodation_type=accommodation_type,
            campus=campus,
            agency=agency,
            room_size=room_size,
            furnished=furnished,
            location=location
            )
        order.save()
        return order 


