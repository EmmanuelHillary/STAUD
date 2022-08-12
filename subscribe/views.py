from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from .models import Subscribe
from .serializers import SubscribeSerializer
from rest_framework.response import Response
from .mail import unsubscribe_email

class SubscribeAPIView(APIView):
    def get(self, *args, **kwargs):
        qs = Subscribe.objects.all()
        serializer = SubscribeSerializer(qs, many=True).data
        return Response({'serializer': serializer})
    
    def post(self, *args, **kwargs):
        data = self.request.data
        serialized_data = SubscribeSerializer(data=data, context={'request': self.request})
        if serialized_data.is_valid():
            serialized_data.save()
            return Response({"message": "Check your email for Confirmation"})
        else:
            return Response({"error": serialized_data.errors})


class SubConfirmAPIView(APIView):
    def get(self, *args, **kwargs):
        obj = Subscribe.objects.get(email=self.request.GET.get("email"))
        if obj.conf_num == self.request.GET.get("conf_num"):  
            obj.confirmed = True
            obj.save()
            return Response({"msg": "You Have Successfully Subscribed to STAUD Newsletter"})
        else:
            return Response({"msg": "Your Subscription to STAUD Newsletter was Unsuccessful"})

class UnsubscribeAPIView(APIView):
    def get(self, *args, **kwargs):
        email = self.request.GET.get("email")
        obj = Subscribe.objects.get(email=email)
        if obj.conf_num == self.request.GET.get("conf_num"):  
            obj.delete()
            unsubscribe_email(email)
            return Response({"msg": "You Have Successfully Unsubscribed to STAUD Newsletter"})
        else:
            return Response({"msg": "Your Unsubscription to STAUD Newsletter was Unsuccessful"})
        

