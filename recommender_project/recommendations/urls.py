# recommendations/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.recommend_tshirts, name='recommend_tshirts'),
]
