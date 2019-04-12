from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('welcome/', views.welcome ),
    path('now/', views.shownow ),
    path('countries/', views.show_countries),
    path('discount/', views.calculate_discount),
]
