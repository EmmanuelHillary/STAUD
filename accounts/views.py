# from .serializers import UserRegisterSerializer
from .permissions import AnonPermission
from rest_framework.permissions import AllowAny
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework.response import Response
from .serializers import ACCOUNT_TYPE, AGENCY
from .models import Agent
from django.db.models import Q
from datetime import date
from accommodation.models import Accommodation
from accommodation.serializers import AccommodationAPISerializer
from django.contrib.auth import authenticate, login, logout


class RegisterAPIView(APIView): 
    permission_classes = [AllowAny]
    
    def get(self, *args, **kwargs):
        data = {
            "account_type": ACCOUNT_TYPE,
            "agency": AGENCY
        }
        return Response(data)

    # def post(self, *args, **kwargs):
    #     data = self.request.data
    #     serialized_data = UserRegisterSerializer(data=data, context={"request": self.request})
    #     if serialized_data.is_valid():
    #         serialized_data.save()
    #         return Response({"success": "Check your email for Confirmation"})
    #     else:
    #         return Response({"error": serialized_data.errors})

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

class RegisterConfirmAPIView(APIView):
    def get(self, *args, **kwargs):
        obj = Agent.objects.get(email=self.request.GET.get("email"))
        if obj.conf_num == self.request.GET.get("conf_num"):  
            obj.email_verification = True
            obj.save()
            return Response({"msg": "Your Email Has Been Successfully Confirmed"})
        else:
            return Response({"msg": "Your Email Confirmation was Unsuccessful"})

class LoginAPIView(APIView):
    permission_classes = [AllowAny]    
    def post(self, request, *args, **kwargs):
        logout(request)
        data = request.data
        username = data.get('username')
        password = data.get('password')
        qs = User.objects.filter(
            Q(username__iexact=username)|
            Q(email__iexact=username)
        ).distinct()
        if qs.exists():
            user_obj = qs.first()
            if user_obj.check_password(password):
                user = authenticate(username=user_obj.username, password=password)
                login(request, user)
                data = {
                    "success": {
                        "username": user_obj.username
                    }
                }
                return Response(data)
            else:
                return Response({"error": {"password":"Invalid Password"}})
        return Response({"error": {"username":"Invalid Username"}})

class AgentDetailAPIView(APIView):
    def get(self, *args, **kwargs):
        username = self.kwargs.get("username")
        obj = Agent.objects.get(username=username)
        if obj and obj.username == self.request.user.username:
            first_name = obj.first_name
            last_name = obj.last_name
            today = date.today().strftime("%d %b, %Y")
            qs = Accommodation.objects.filter(agent=obj).order_by("-number_of_views")[:2]
            data = {
                "first_name": first_name,
                "last_name": last_name,
                "email_verification":obj.email_verification,
                "today": today,
                "most_staud_clicks": AccommodationAPISerializer(qs, many=True).data
            }
            return Response(data)
        return Response({"error": "Unauthorised Access Error 403"}, status=403)

class AgentListingsAPIView(APIView):
    def get(self, *args, **kwargs):
        username = self.kwargs.get("username")
        obj = Agent.objects.get(username=username)
        if obj and obj.username == self.request.user.username:
            qs = Accommodation.objects.filter(agent=obj).order_by("-updated")
            data = {
                "staud_listings": AccommodationAPISerializer(qs, many=True).data
            }
            return Response(data)
        return Response({"error": "Unauthorised Access Error 403"}, status=403)





