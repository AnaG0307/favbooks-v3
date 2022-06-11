from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Book, Sub_Category
from .forms import BookForm


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
            books = books.filter(
                book_sub_category__book_sub_category__in=book_sub_categories
                )
            book_sub_categories = Sub_Category.objects.filter(
                book_sub_category__in=book_sub_categories
                )

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


@login_required
def add_book(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners \
            can access this page.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('book_detail', args=[book.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the \
                form is valid.')
    else:
        form = BookForm()

    template = 'books/add_book.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_book(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can access \
            this page.')
        return redirect(reverse('home'))

    book = get_object_or_404(Book, pk=product_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated book!')
            return redirect(reverse('book_detail', args=[book.id]))
        else:
            messages.error(request, 'Failed to update book. Please ensure the \
                form is valid.')
    else:
        form = BookForm(instance=book)
        messages.info(request, f'You are editing {book.title}')

    template = 'books/edit_book.html'
    context = {
        'form': form,
        'book': book,
    }

    return render(request, template, context)


@login_required
def delete_book(request, product_id):
    """ Delete a book from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can access \
            this page.')
        return redirect(reverse('home'))

    book = get_object_or_404(Book, pk=product_id)
    book.delete()
    messages.success(request, 'Book deleted!')
    return redirect(reverse('books'))
