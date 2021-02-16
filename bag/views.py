from django.shortcuts import render


def view_bag(request):
    '''A view to return the user's shopping bag items'''
    return render(request, 'bag/bag.html')
