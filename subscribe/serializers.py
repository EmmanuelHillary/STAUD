from rest_framework import serializers
from django.shortcuts import reverse
from .models import Subscribe
import re
import random
from .mail import subscribe_email
from django.conf import settings

def random_digits():
    return "%0.12d" % random.randint(0, 999999999999)


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = ["email"]
        extra_kwargs = {
        'email': {
            'error_messages': {
                'blank': 'Email is required.',
            }
        }
    }
    
    def validate_email(self, value):
        obj = Subscribe.objects.filter(email=value.lower())
        if value is None:
            raise serializers.ValidationError("Email is required.")
        elif obj.exists():
            raise serializers.ValidationError('Email Address already exists')
        elif not re.match(r"^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$", value):
            raise serializers.ValidationError('Invalid Email Address')
        return value
    
    def create(self, validated_data):
        email = validated_data.get("email")
        conf_number=random_digits()
        request = self.context.get("request")
        url = request.build_absolute_uri(reverse('staud:subscribe_confirmation'))
        subscribe_email(email, conf_number, url)
        obj = Subscribe.objects.create(
            email=email,
            conf_num=conf_number
        )
        return obj

