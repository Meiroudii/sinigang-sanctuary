from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "blog/index.html")

def about(request):
    return render(request, "blog/about.html")

def contact(request):
    return render(request, "blog/about.html")

def restaurant_reviews(request):
    return render(request, "blog/restaurantReviews.html")
