from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from books.models import Book


def view_bag(request):
    """ View to return the contents of the bag """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ View to add quantity of a specific book to the shopping bag """

    product = Book.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
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

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ View to remove a specific book from the shopping bag """

    try:
        bag = request.session.get('bag', {})

        bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
