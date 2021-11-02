from .models import Agent
from rest_framework import serializers

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