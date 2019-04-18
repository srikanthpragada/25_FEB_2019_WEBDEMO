from django.shortcuts import render, redirect

from .forms import BookForm
from .models import Book


def book_delete(request, id):
    try:
        book = Book.objects.get(id=id)
        book.delete()
        return redirect("/demo/book/list")
    except:
        return render(request, 'book_delete.html',
                      {'message': f"Book With ID {id} Not Found!"})


def book_edit(request, id):
    if request.method == "GET":
        try:
            book = Book.objects.get(id=id)
            f = BookForm(instance=book)
            return render(request, 'book_edit.html', {'form': f})
        except:
            return render(request, 'book_edit.html',
                          {'message': f"Book With ID {id} Not Found!"})
    else: # Post
        # Update book
        book = Book.objects.get(id=id)
        f = BookForm(request.POST, instance=book)
        f.save() # Updation
        return redirect("/demo/book/list")


def book_add(request):
    message = ""
    if request.method == "GET":
        f = BookForm()
    else:  # Post
        f = BookForm(request.POST)  # Bind input data with form
        if f.is_valid():
            f.save();  # Insert object into table
            message = "Book has been added!"
        else:
            message = "Sorry! Invalid data. Try again!"

    return render(request, 'book_add.html',
                  {'form': f, 'message': message})


def book_summary(request):
    book_count = Book.objects.all().count()
    return render(request, 'book_summary.html',
                  {"count": book_count})


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html',
                  {"books": books})
