from django.urls import path

from . import views

urlpatterns = [
        path("", views.index, name="index"),
        path("about/", views.about, name="about"),
        path("schnitzel/", views.dish_readmore, name="dish_readmore"),
        path("restaurant-reviews/", views.restaurant_reviews, name="restuarant_reviews"),
        ]
