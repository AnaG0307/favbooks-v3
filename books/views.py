from django.shortcuts import render
from .models import Book


def all_books(request):
    """ View to return return all books, sorting and search queries """

    books = Book.objects.all()

    context = {
        'books': books,
    }

    return render(request, 'books/books.html', context)
