from .models import Agent
from rest_framework import serializers
from .mail import email_confirmation
from company.models import Company
from django.contrib.auth.models import User 
import re
import random
from django.shortcuts import reverse

ACCOUNT_TYPE = [
    'Estate Agent',
    'Property Developer',
    'Property Owner',
]

AGENCY = ["None"] + [str(agency) for agency in Company.objects.all()]

def random_digits():
    return "%0.12d" % random.randint(0, 999999999999)

class AgentSerializer(serializers.ModelSerializer):
    company = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Agent
        fields = [
            'first_name', 
            'last_name',
            'display_picture',
            'mobile_number', 
            'whatsapp_number',
            'company', 
            'staud_rating',
        ]
    
    def get_company(self, obj):
        return obj.company.name