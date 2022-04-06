from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Book, Sub_Category


def all_books(request):
    """ View to return all books, sorting and search queries """

    books = Book.objects.all()
    query = None
    book_sub_categories = None
    sort = None
    direction = None

    if request.GET:
        # sorting by price, rating and product name functionality
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                books = books.annotate(lower_name=Lower('name'))

            if sortkey == 'book_sub_category':
                sortkey = 'book_sub_category__book_sub_category'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            books = books.order_by(sortkey)

        # sorting by sub_category functionality
        if 'book_sub_category' in request.GET:
            book_sub_categories = request.GET['book_sub_category'].split(',')
            books = books.filter(book_sub_category__book_sub_category__in=book_sub_categories)
            book_sub_categories = Sub_Category.objects.filter(book_sub_category__in=book_sub_categories)

        # search functionality
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search criteria entered!")
                return redirect(reverse('books'))

            queries = Q(title__icontains=query) | Q(synopsis__icontains=query) | Q(author__icontains=query)
            books = books.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'books': books,
        'search_term': query,
        'current_sub_categories': book_sub_categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'books/books.html', context)


def book_detail(request, book_id):
    """ View to return details of a single book in full """

    book = get_object_or_404(Book, pk=book_id)

    context = {
        'book': book,
    }

    return render(request, 'books/book_detail.html', context)
