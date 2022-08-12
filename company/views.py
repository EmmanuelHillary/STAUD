from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .serializers import CompanySerializer, CompanyDetailSerializer
from accommodation.serializers import (CAMPUS, ACCOMMODATION_TYPE, FURNISHED, PRICE, ROOM_SIZE)
from .models import Company
from django.shortcuts import get_object_or_404

class CompanyListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q') or None
        qs = Company.objects.all().order_by("-updated")
        if query is not None:
            qs = Company.objects.filter(name__icontains=query).order_by("-updated")
        
        data = {
            "accommodation_type": ACCOMMODATION_TYPE,
            "campus": CAMPUS,
            "price": PRICE,
            "room_size": ROOM_SIZE,
            "furnished": FURNISHED,
            "company": CompanySerializer(qs, many=True).data
        }
        return Response(data)

class  CompanyDetailAPIView(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyDetailSerializer


