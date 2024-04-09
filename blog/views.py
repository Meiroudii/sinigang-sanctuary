from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(request):
    return render(request, "blog/index.html")

def about(request):
    return render(request, "blog/about.html")

# TODO: Add url arguments!!!
def dish_readmore(request):
    post = Post.objects.get(id=1)
    return render(request, "blog/foods_templates/schnitzel.html", {
        'post': post,
        })

def restaurant_reviews(request):
    return render(request, "blog/restaurantReviews.html")
