from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Book

# Converts Book objects to JSON
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'price')


def rest_client(request):
    return render(request, 'rest_client.html')


@api_view(['GET', 'POST'])
def get_post_books(request):
    if request.method == "GET":
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        # send all titles in the form of json
        return Response(serializer.data)
    else:  # POST, so insert a new row into table
        book = BookSerializer(data=request.data)
        if book.is_valid():
            book.save()  # insert into table
            return Response(book.data)
        else:
            return Response(book.errors, status=400)  # bad request


@api_view(['GET', 'DELETE'])
def get_delete_one_book(request, id):
    # check whether object is found
    try:
        book = Book.objects.get(id=id)
    except:
        return Response(status=404)  # Send 404 to client

    if request.method == "GET":
        # Convert Python object to Json and send to client
        serializer = BookSerializer(book)
        return Response(serializer.data)
    else:  # Delete object from Table and send 204 as status code
        book.delete()
        return Response(status=204)  # No data
