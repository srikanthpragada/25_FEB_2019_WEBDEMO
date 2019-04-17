from django.shortcuts import render

from .models import Book


def book_summary(request):
    book_count = Book.objects.all().count()
    return render(request, 'book_summary.html',
                  {"count": book_count})


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html',
                  {"books": books})
