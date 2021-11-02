from django.urls import path
from .views import (ApartmentAPIView, AccommodationsAPIView, HostelAPIView,
 MostSoldStaudAPIView, MostViewedStaudAPIView, AccommodationDetailAPIView)

app_name = "accommodation"

urlpatterns = [
    path('', AccommodationsAPIView.as_view(), name="accommodations"),
    path('<int:pk>/', AccommodationDetailAPIView.as_view(), name="detail"), 
    path('hostels/', HostelAPIView.as_view(), name="hostel"),
    path('apartments/', ApartmentAPIView.as_view(), name="apartment"),
    path('most-searched/', MostViewedStaudAPIView.as_view(), name="most-searched"),
    path('most-sold/', MostSoldStaudAPIView.as_view(), name="most-sold"),
    
]