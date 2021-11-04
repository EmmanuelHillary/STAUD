from django.shortcuts import render

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

def privacy_terms(request):
    return render(request, "privacy&terms/index.html")



