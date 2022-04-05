from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Book, Sub_Category


def all_books(request):
    """ View to return all books, sorting and search queries """

    books = Book.objects.all()
    query = None
    book_sub_categories = None

    if request.GET:
        if 'book_sub_category' in request.GET:
            book_sub_categories = request.GET['book_sub_category'].split(',')
            books = books.filter(book_sub_category__book_sub_category__in=book_sub_categories)
            book_sub_categories = Sub_Category.objects.filter(book_sub_category__in=book_sub_categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search criteria entered!")
                return redirect(reverse('books'))

            queries = Q(title__icontains=query) | Q(synopsis__icontains=query) | Q(author__icontains=query)
            books = books.filter(queries)

    context = {
        'books': books,
        'search_term': query,
        'current_sub_categories': book_sub_categories,
    }

    return render(request, 'books/books.html', context)


def book_detail(request, book_id):
    """ View to return details of a single book in full """

    book = get_object_or_404(Book, pk=book_id)

    context = {
        'book': book,
    }

    return render(request, 'books/book_detail.html', context)
