from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from accommodation.serializers import (AccommodationAPISerializer, AccommodationDetailSerializer,
CAMPUS, ACCOMMODATION_TYPE, FURNISHED, PRICE, ROOM_SIZE)
from accommodation.models import Campus, Accommodation
from django.db.models import Q 
import re


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