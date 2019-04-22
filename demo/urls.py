from django.contrib import admin
from django.urls import path, include
from . import views, book_views, rest_views

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
    path('book/searchform/', book_views.book_searchform),
    path('book/search/<title>', book_views.book_search),
    path('book/delete/<int:id>', book_views.book_delete),
    path('book/edit/<int:id>', book_views.book_edit),
    path('today/', views.today),
    path('ajax/', views.ajax_demo),
    path('cookies/', views.cookie_city),
    path('sessions/', views.session_city),
    # Rest API urls
    path('api/books/', rest_views.get_post_books),
    path('api/books/<int:id>', rest_views.get_delete_one_book),
    path('api/client', rest_views.rest_client),
]
