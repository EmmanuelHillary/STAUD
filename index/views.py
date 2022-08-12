from rest_framework.views import APIView
from rest_framework.response import Response
from accommodation.serializers import AccommodationAPISerializer, CAMPUS, ACCOMMODATION_TYPE, PRICE
from accommodation.models import Campus, Accommodation



class IndexAPIView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Accommodation.objects.get_featured_staud().order_by("-updated")[:10] or None
        if qs is None:
            qs = Accommodation.objects.all().order_by("-updated")[:10]
        featured_staud = AccommodationAPISerializer(qs, many=True)
        data = { 
            "accommodation_type": ACCOMMODATION_TYPE,
            "campus": CAMPUS,
            "price": PRICE,
            "featured_staud": featured_staud.data
        }
        
        return Response(data)






        



