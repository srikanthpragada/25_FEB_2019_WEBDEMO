from django.contrib import admin
from django.urls import path, include
from . import views, book_views

urlpatterns = [
    path('welcome/', views.welcome ),
    path('now/', views.shownow ),
    path('countries/', views.show_countries),
    path('discount/', views.calculate_discount),
    path('discount2/', views.calculate_discount_post),
    path('interest/', views.calculate_interest),
    path('book/summary/', book_views.book_summary),
    path('book/list/', book_views.book_list),
    path('book/add/', book_views.book_add),
    path('book/delete/<int:id>', book_views.book_delete),
    path('book/edit/<int:id>', book_views.book_edit),
]
