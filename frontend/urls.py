from django.urls import path
from .views import (home, accommodations, apartments, hostels, most_viewed,
 most_sold, company, order, order_successful, accommodation_detail, company_detail, login, register,
 about_FAQ, contact_us, privacy_terms, contact_us_successful, subscribe_confirmation, logout_view,
 subscribe_unsubscribe, agent_email_confirmation, agent_dashboard, agent_listings, agent_poststaud, agent_poststaud_edit, agent_profile
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
    path("order/successful/", order_successful, name="order_successful"),
    path("accommodation/<int:pk>/", accommodation_detail, name="accommodation_detail"),
    path("company/<int:pk>/", company_detail, name="company_detail"),
    path("sign-in/", login, name="login"),
    path("register/", register, name="register"),
    path("about-FAQ/", about_FAQ, name="about-FAQ"),
    path("contact-us/", contact_us, name="contact-us"),
    path("privacy-terms/", privacy_terms, name="privacy-terms"),
    path("contact-us/successful/", contact_us_successful, name="contact_successful"),
    path("subscribe/confirmation/", subscribe_confirmation, name="subscribe_confirmation"),
    path("unsubscribe/", subscribe_unsubscribe, name="subscribe_unsubscribe"),
    path("agent/confirmation/", agent_email_confirmation, name="agent_email_confirmation"),
    path("agent/dashboard/<str:username>/", agent_dashboard, name="agent_dashboard"),
    path("agent/dashboard/<str:username>/profile/", agent_profile, name="agent_profile"),
    path("agent/dashboard/<str:username>/listings/", agent_listings, name="agent_listings"),
    path("agent/dashboard/<str:username>/post-staud/", agent_poststaud, name="agent_poststaud"),
    path("agent/dashboard/<str:username>/edit-staud/<int:pk>/", agent_poststaud_edit, name="agent_poststaud_edit"),
    path("agent/logout/", logout_view, name="logout"),
]