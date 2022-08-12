from django.urls import path
from .views import CompanyListAPIView, CompanyDetailAPIView

app_name = "company"

urlpatterns = [
    path("", CompanyListAPIView.as_view(), name="list"),
    path("<int:pk>/", CompanyDetailAPIView.as_view(), name="detail")
]