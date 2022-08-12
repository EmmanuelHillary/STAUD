from django.shortcuts import render, redirect
from django.contrib.auth import logout

def home(request):
    return render(request, "home/index.html")

def accommodations(request):
    return render(request, "home/accommodations.html")

def apartments(request):
    return render(request, "houses/apartments.html")

def hostels(request):
    return render(request, "hostels/hostels.html")

def most_viewed(request):
    return render(request, "home/most_viewed.html")

def most_sold(request):
    return render(request, "home/most_sold.html")

def company(request):
    return render(request, "companies/index.html")

def order(request):
    return render(request, "orders/index.html")

def order_successful(request):
    return render(request, "orders/successful.html")

def accommodation_detail(request, pk):
    return render(request, "hostels-view/index.html")

def company_detail(request, pk):
    return render(request, "companies-view/index.html")

def login(request):
    return render(request, "agent-signin/index.html")

def register(request):
    return render(request, "registration/index.html")

def contact_us(request):
    return render(request, "contact/index.html")

def contact_us_successful(request):
    return render(request, "contact/successful.html")

def about_FAQ(request):
    return render(request, "about&faQ/index.html")

def subscribe_confirmation(request):
    return render(request, "subscribe/confirm_email.html")

def subscribe_unsubscribe(request):
    return render(request, "subscribe/unsubscribe.html")

def privacy_terms(request):
    return render(request, "privacy&terms/index.html")

def agent_email_confirmation(request):
    return render(request, "agent/confirmation_email.html")

def agent_dashboard(request, username):
    return render(request, "agent-dashboard/index.html")

def agent_listings(request, username):
    return render(request, "agent-listings/index.html")

def agent_poststaud(request, username):
    return render(request, "agent-poststaud/index.html")

def agent_poststaud_edit(request, username, pk):
    return render(request, "agent-poststaud/edit.html")

def agent_profile(request, username):
    return render(request, "agent-profile/index.html")

def logout_view(request):
    logout(request)
    return redirect("staud:homepage")

