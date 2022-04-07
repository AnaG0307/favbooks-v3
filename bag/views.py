from django.shortcuts import render


def view_bag(request):
    """ View to return the contents of the bag """

    return render(request, 'bag/bag.html')
