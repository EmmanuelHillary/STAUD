from django.urls import path
from .views import (home, accommodations, apartments, hostels, most_viewed,
 most_sold, company, order, order_successful, accommodation_detail, company_detail, login, register,
 about_FAQ, contact_us, privacy_terms
 )

app_name = "staud"

urlpatterns = [
    path("", home, name="homepage"),
    path("accommodations/", accommodations, name="accommodations"),
    path("apartments/", apartments, name="apartments"),
    path("hostels/", hostels, name="hostels"),
    path("most-searched/", most_viewed, name="most-searched"),
    path("most-sold/", most_sold, name="most-sold"),
    path("companies/", company, name="company"),
    path("order/", order, name="order"),
    path("order/successful", order_successful, name="order_successful"),
    path("accommodation/<int:pk>/", accommodation_detail, name="accommodation_detail"),
    path("company/<int:pk>/", company_detail, name="company_detail"),
    path("sign-in/", login, name="login"),
    path("register/", register, name="register"),
    path("about-FAQ/", about_FAQ, name="about-FAQ"),
    path("contact-us/", contact_us, name="contact-us"),
    path("privacy-terms/", privacy_terms, name="privacy-terms"),
]