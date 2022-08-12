from rest_framework import serializers
from .models import Contact
from .mail import contact_us

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"
    
    def create(self, validated_data):
        name = validated_data.get('name')
        email = validated_data.get('email')
        message = validated_data.get('message')
        contact_us(name, email, message)
        contact = Contact.objects.create(**validated_data)
        contact.save()
        return contact

