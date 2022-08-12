from django.urls import path
from .views import RegisterAPIView, RegisterConfirmAPIView, LoginAPIView, AgentDetailAPIView, AgentListingsAPIView

app_name = "accounts"

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name="login"),
    path('register/', RegisterAPIView.as_view(), name="register"),
    path('email/confirm/', RegisterConfirmAPIView.as_view(), name="email_confirm"),
    path('<str:username>/', AgentDetailAPIView.as_view(), name="detail"),
    path('<str:username>/listings/', AgentListingsAPIView.as_view(), name="listings")
]

