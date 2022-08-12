from django.urls import path
from .views import OrderListCreateAPIView

app_name = "order"

urlpatterns = [
    path("", OrderListCreateAPIView.as_view(), name="create")
]