from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
    )
from django.contrib import messages
from books.models import Book


def view_bag(request):
    """ View to return the contents of the bag """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ View to add quantity of a specific book to the shopping bag """

    product = get_object_or_404(Book, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(
            request,
            f'Updated quantity of {product.title} by \
            {product.author} to your bag'
            )
    else:
        bag[item_id] = quantity
        messages.success(
            request,
            f'Added {product.title} by {product.author} to your bag'
            )

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ View to adjust quantity of a specific book in the shopping bag """

    product = get_object_or_404(Book, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request,
            f'Updated quantity of {product.title} by \
                {product.author} to {bag[item_id]}'
            )
    else:
        bag.pop(item_id)
        messages.success(
            request,
            f'Removed {product.title} by {product.author} from your bag'
            )

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ View to remove a specific book from the shopping bag """

    try:
        product = get_object_or_404(Book, pk=item_id)
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(
            request,
            f'Removed {product.title} by {product.author} from your bag'
            )

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
