from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from accommodation.serializers import (AccommodationAPISerializer, AccommodationDetailSerializer,
CAMPUS, ACCOMMODATION_TYPE, FURNISHED, PRICE, ROOM_SIZE, AccommodationEditDetailSerializer)
from .create_staud import  (CAMPUS_INFO, ACCOMMODATION_INFO, FURNISHED_INFO, SEX_INFO,
                            MARKET_STATUS_INFO, ROOM_SIZE_INFO, ACCOMMODATION_TYPE_INFO, create_staud_id, create_staud, edit_staud)
from accommodation.models import Campus, Accommodation
from accounts.models import Agent
from django.db.models import Q 
from .models import Accommodation, AccommodationInfo, TopFeature, AccommodationImage
import re
from rest_framework.parsers import MultiPartParser, FormParser



class AccommodationsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        
        address = request.GET.get('address') or None
        acc_type = [request.GET.get('type')]
        if acc_type == ['All Types']:
            acc_type = ['Apartment', 'Hostel']
        campus = [request.GET.get('campus')]
        c = []
        for i in Campus.objects.all():
            c.append(i.name)
        if campus == ['All Schools']:
            campus = c
        price_range = request.GET.get('price')
        if price_range == 'No Range':
            price_range = [0.00]
            p = Q(price__gte=0)
        else:
            price_range = [int(s) for s in re.findall('\d+', price_range.replace(',', ''))]

            if price_range == [500000]:
                p = Q(price__gte=500000)
            elif price_range == [100000]:
                p = Q(price__lte=100000)
            else:
                p = Q(price__lte=price_range[0]) & Q(price__gte=price_range[1])
        room_size = [request.GET.get('room_size')] or None
        if room_size == ['Any Size']:
            room_size = ROOM_SIZE 
        furnished = [request.GET.get('furnished')] or None
        if furnished == ['All Options']:
            furnished = ['Yes', 'No']
        if address is None or address == "null":
            qs=Accommodation.objects.filter(
                Q(accommodation_type__in=acc_type) &
                Q(campus__name__in=campus) &
                Q(furnished__in=furnished) &
                Q(room_size__in=room_size) &
                p
                ).distinct() 
        else:
            qs=Accommodation.objects.filter(
                Q(address__icontains=address) &
                Q(accommodation_type__in=acc_type) &
                Q(campus__name__in=campus) &
                Q(furnished__in=furnished) &
                Q(room_size__in=room_size) &
                p
                ).distinct()
        
        print(qs)
        date = Accommodation.objects.all().order_by("-updated").first().created
        accommodation = AccommodationAPISerializer(qs, many=True)
        data = { 
            "update": date.strftime("%d %b, %Y"),
            "accommodation_type": ACCOMMODATION_TYPE,
            "campus": CAMPUS,
            "price": PRICE,
            "room_size": ROOM_SIZE,
            "furnished": FURNISHED,
            "accommodation": accommodation.data
        }
        
        return Response(data)


class ApartmentAPIView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Accommodation.objects.get_all_apartments().order_by("-updated")
        date = Accommodation.objects.all().order_by("-updated").first().created
        data = { 
            "update": date.strftime("%d %b, %Y"),
            "accommodation_type": ACCOMMODATION_TYPE,
            "campus": CAMPUS,
            "price": PRICE,
            "room_size": ROOM_SIZE,
            "furnished": FURNISHED,
            "accommodation": AccommodationAPISerializer(qs, many=True).data
        }
        return Response(data)  

class HostelAPIView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Accommodation.objects.get_all_hostels().order_by("-updated")
        date = Accommodation.objects.all().order_by("-updated").first().created
        data = { 
            "update": date.strftime("%d %b, %Y"),
            "accommodation_type": ACCOMMODATION_TYPE,
            "campus": CAMPUS,
            "price": PRICE,
            "room_size": ROOM_SIZE,
            "furnished": FURNISHED,
            "accommodation": AccommodationAPISerializer(qs, many=True).data
        }
        return Response(data)

class AccommodationDetailAPIView(generics.RetrieveAPIView):
    queryset = Accommodation.objects.all()
    serializer_class = AccommodationDetailSerializer

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.number_of_views += 1
        obj.save()
        data = AccommodationDetailSerializer(obj).data
        return Response(data)

class MostViewedStaudAPIView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Accommodation.objects.all().order_by("-number_of_views")[:10]
        date = Accommodation.objects.all().order_by("-updated").first().created
        data = { 
            "update": date.strftime("%d %b, %Y"),
            "accommodation_type": ACCOMMODATION_TYPE,
            "campus": CAMPUS,
            "price": PRICE,
            "room_size": ROOM_SIZE,
            "furnished": FURNISHED,
            "accommodation": AccommodationAPISerializer(qs, many=True).data
        }
        return Response(data)  

class MostSoldStaudAPIView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Accommodation.objects.all().order_by("-units_sold")[:10]
        date = Accommodation.objects.all().order_by("-updated").first().created
        data = { 
            "update": date.strftime("%d %b, %Y"),
            "accommodation_type": ACCOMMODATION_TYPE,
            "campus": CAMPUS,
            "price": PRICE,
            "room_size": ROOM_SIZE,
            "furnished": FURNISHED,
            "accommodation": AccommodationAPISerializer(qs, many=True).data
        }
        return Response(data)

class STAUDCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser,)
    username = None
    def get(self, request, *args, **kwargs): 
        self.username = self.kwargs.get("username")
        agent = Agent.objects.filter(username=self.username)
        if agent and self.request.user.username == self.username:
            data = { 
            "accommodation_type": ACCOMMODATION_TYPE_INFO,
            "campus": CAMPUS_INFO,
            "property_name": ACCOMMODATION_INFO, 
            "room_size": ROOM_SIZE_INFO,
            "furnished": FURNISHED_INFO,
            "sex": SEX_INFO,
            "market_status": MARKET_STATUS_INFO,
            }
            return Response(data)
        else:
            return Response({"error": "Unauthorised Access Error 403"}, status=403)
    
    def post(self, request, *args, **kwargs):
        username = self.kwargs.get("username")
        agent = Agent.objects.filter(username=username)
        if agent and self.request.user.username == username:
            agent= agent.first()
            data = request.data
            print(data)
            name = data.get("property_name")
            accommodation_type = data.get("accommodation_type")
            campus = data.get("campus")
            room_size = data.get("room_size")
            furnished = data.get("furnished")
            sex = data.get("sex")
            market_status = data.get("market_status")
            address = data.get("address")
            price = data.get("price")
            short_description = data.get("short_description")
            full_description = data.get("full_description")
            features = None
            if data.get("features"):
                features = data.getlist("features")
            images = data.getlist("images") 
            create_staud(agent, name, accommodation_type, campus, room_size, furnished, sex, market_status, address, price, short_description, full_description, features, images)
            return Response({"msg": "it worked"})
        return Response({"error": "UnAuthorised Access Error 403"})

class STAUDEditAPIView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser,)
    def get(self, request, *args, **kwargs):
        obj_id = self.kwargs.get("pk")
        obj = Accommodation.objects.get(id=obj_id)
        accommodation = AccommodationEditDetailSerializer(obj).data
        agent = Agent.objects.filter(username=obj.agent.username)
        if agent and self.request.user.username == obj.agent.username:
            data = { 
            "accommodation_type": ACCOMMODATION_TYPE_INFO,
            "campus": CAMPUS_INFO, 
            "room_size": ROOM_SIZE_INFO,
            "furnished": FURNISHED_INFO,
            "sex": SEX_INFO,
            "market_status": MARKET_STATUS_INFO,
            "accommodation": accommodation
            }
            return Response(data)
        else:
            return Response({"error": "Unauthorised Access Error 403"}, status=403)
    
    def post(self, request, *args, **kwargs):
        obj_id = self.kwargs.get("pk")
        obj = Accommodation.objects.get(id=obj_id)
        accommodation = AccommodationEditDetailSerializer(obj).data
        agent = Agent.objects.filter(username=obj.agent.username)
        if agent and self.request.user.username == obj.agent.username:
            agent= agent.first()
            data = request.data
            name = data.get("property_name")
            accommodation_type = data.get("accommodation_type")
            campus = data.get("campus")
            room_size = data.get("room_size")
            furnished = data.get("furnished")
            sex = data.get("sex")
            market_status = data.get("market_status")
            address = data.get("address")
            price = data.get("price")
            short_description = data.get("short_description")
            full_description = data.get("full_description")
            features = None
            if data.get("features"):
                features = data.getlist("features")
            images = None
            if data.get("images"):
                images = data.getlist("images") 
            edit_staud(agent, name, obj_id, accommodation_type, campus, room_size, furnished, sex, market_status, address, price, short_description, full_description, features, images)
            return Response({"msg": "it worked"})
        return Response({"error": "UnAuthorised Access Error 403"})

class STAUDDeleteAPIView(APIView):
    def post(self, request, *args, **kwargs):
        obj_id = self.kwargs.get("pk")
        obj = Accommodation.objects.get(id=obj_id)
        agent = Agent.objects.filter(username=obj.agent.username)
        if agent and self.request.user.username == obj.agent.username:
            obj.delete()
            data = { 
            "msg": "accommodation deleted"
            }
            return Response(data)
        else:
            return Response({"error": "Unauthorised Access Error 403"}, status=403)