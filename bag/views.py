from django.shortcuts import render, redirect


def view_bag(request):
    """ View to return the contents of the bag """

    return render(request, 'bag/bag.html')


    # View to add quantity of a specific book to the shopping bag
def add_to_bag(request, item_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
