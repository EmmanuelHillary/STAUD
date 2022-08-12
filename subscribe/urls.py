from django.urls import path
from .views import SubscribeAPIView, SubConfirmAPIView, UnsubscribeAPIView

app_name = "subscribe"

urlpatterns = [
    path("", SubscribeAPIView.as_view(), name="subscribe"),
    path("confirm/", SubConfirmAPIView.as_view(), name="confirm"),
    path("unsubscribe/", UnsubscribeAPIView.as_view(), name="unsubscribe"),

]