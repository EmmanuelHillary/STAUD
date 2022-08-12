from django.urls import path
from .views import ContactAPIView

app_name = "contact"

urlpatterns = [
    path('', ContactAPIView.as_view(), name="contact")
]