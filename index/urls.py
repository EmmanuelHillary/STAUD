from django.urls import path
from .views import IndexAPIView

app_name = "index"

urlpatterns = [
    path('', IndexAPIView.as_view(), name="home"), 
]