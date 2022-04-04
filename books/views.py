from django.shortcuts import render, get_object_or_404
from .models import Book


def all_books(request):
    """ View to return all books, sorting and search queries """

    books = Book.objects.all()

    context = {
        'books': books,
    }

    return render(request, 'books/books.html', context)


def book_detail(request, book_id):
    """ View to return details of a single book in full """

    book = get_object_or_404(Book, pk=book_id)

    context = {
        'book': book,
    }

    return render(request, 'books/book_detail.html', context)
