from rest_framework import serializers
from .models import Campus, Accommodation, AccommodationImage, AccommodationInfo
import json
from accounts.serializers import AgentSerializer


CAMPUS = ['All Schools'] 

CAMPUS += [str(campus) for campus in Campus.objects.all()]

ACCOMMODATION_TYPE = [
    'All Types',
    'Apartment', 
    'Hostel'
]

PRICE = [
    'No Range',
    'N500,000 and above', 
    'Between N500,000 and N400,000', 
    'Between N400,000 and N300,000', 
    'Between N300,000 and N200,000', 
    'Between N200,000 and N100,000', 
    'N100,000 and below'
    ]

FURNISHED = [
    'All Options',  
    'Yes', 
    'No', 
]

ROOM_SIZE = [
    'Any Size', 
    'One man room', 
    'Two man room', 
    'Three man room', 
    'Four man room', 
    'Six man room', 
    'Eight man room',
    'Miniflat', 
    'Self contain'
]




class AccommodationAPISerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    address = serializers.SerializerMethodField(read_only=True)
    short_desc = serializers.SerializerMethodField(read_only=True)
    uri = serializers.SerializerMethodField(read_only=True)
    campus = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Accommodation
        fields = ["id", "name", "accommodation_type", "campus", "address", "short_desc", "display_picture", "uri"]
    
    def get_campus(self, obj):
        name = obj.campus.name
        return name

    def get_name(self, obj):
        name = obj.accommodation.name
        return name
    
    def get_address(self, obj):
        address = obj.address
        return address
    
    def get_short_desc(self, obj):
        short_desc = obj.accommodation.short_description
        return short_desc
    
    def get_uri(Self, obj):
        return ""


class CampusAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Campus
        fields = "__all__"

class AccommodationDetailSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    short_desc = serializers.SerializerMethodField(read_only=True)
    images = serializers.SerializerMethodField(read_only=True)
    top_features = serializers.SerializerMethodField(read_only=True)
    agent = serializers.SerializerMethodField(read_only=True)
    created = serializers.SerializerMethodField(read_only=True)
    updated = serializers.SerializerMethodField(read_only=True)
    acc_type = serializers.SerializerMethodField(read_only=True)
    accommodation_type = serializers.SerializerMethodField(read_only=True)
    campus = serializers.SerializerMethodField(read_only=True)
    price = serializers.SerializerMethodField(read_only=True)
    room_size = serializers.SerializerMethodField(read_only=True)
    furnished = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Accommodation
        fields = [
            'name',
            'short_desc',
            'display_picture',
            'images',
            "full_description",
            "created",
            "updated",
            "staud_id",
            "acc_type",
            "market_status",
            "units_sold",
            "top_features",
            "agent",
            "accommodation_type",
            "campus",
            "price",
            "room_size",
            "furnished"

        ]
    
    def get_name(self, obj):
        name = obj.accommodation.name
        return name

    def get_short_desc(self, obj):
        short_desc = obj.accommodation.short_description
        return short_desc
    
    def get_images(self, obj):
        qs = obj.accommodation_images.all()
        return [ob.images.url for ob in qs]
    
    def get_top_features(self, obj):
        qs = obj.accommodation_top_features.all()
        return [ob.feature for ob in qs]
    
    def get_agent(self, obj):
        return AgentSerializer(obj.agent).data

    def get_created(self, obj):
        return obj.created.strftime("%dth %B, %Y")

    def get_updated(self, obj):
        return obj.updated.strftime("%dth %B, %Y")
    
    def get_acc_type(self, obj):
        return obj.accommodation_type
    
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


class AccommodationEditDetailSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    short_desc = serializers.SerializerMethodField(read_only=True)
    images = serializers.SerializerMethodField(read_only=True)
    top_features = serializers.SerializerMethodField(read_only=True)
    acc_type = serializers.SerializerMethodField(read_only=True)
    market_status = serializers.SerializerMethodField(read_only=True)
    full_description = serializers.SerializerMethodField(read_only=True)
    campus = serializers.SerializerMethodField(read_only=True)
    sex = serializers.SerializerMethodField(read_only=True)
    furnished = serializers.SerializerMethodField(read_only=True)
    room_size = serializers.SerializerMethodField(read_only=True)
    address = serializers.SerializerMethodField(read_only=True)
    price = serializers.SerializerMethodField(read_only=True)
    property_name = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Accommodation
        fields = [
            'name',
            'short_desc',
            'images',
            "full_description",
            "acc_type",
            "market_status",
            "address",
            "top_features",
            "campus",
            "sex",
            "price",
            "furnished",
            "room_size",
            "property_name"

        ]
    
    def get_name(self, obj):
        name = obj.accommodation.name
        return name

    def get_short_desc(self, obj):
        short_desc = obj.accommodation.short_description
        return short_desc
    
    def get_images(self, obj):
        if AccommodationImage.objects.filter(accommodation=obj).exists():
            qs = obj.accommodation_images.all()
            return [ob.images.url for ob in qs]
        return None
    
    def get_top_features(self, obj):
        if obj.accommodation_top_features.all():
            qs = obj.accommodation_top_features.all()
            return [ob.feature for ob in qs]
        return None
    def get_acc_type(self, obj):
        return obj.accommodation_type

    def get_market_status(self, obj):
        return obj.market_status

    def get_full_description(self, obj):
        return obj.full_description

    def get_campus(self, obj):
        return obj.campus.name

    def get_sex(self, obj):
        return obj.sex

    def get_room_size(self, obj):
        return obj.room_size

    def get_furnished(self, obj):
        return obj.furnished
    
    def get_address(self, obj):
        return obj.address
    
    def get_price(self, obj):
        return obj.price
    
    def get_property_name(self, obj):
        return [str(acc.name) for acc in AccommodationInfo.objects.all()]

 
 