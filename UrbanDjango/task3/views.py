from django.shortcuts import render

# Create your views here.


def in_platform(request):
    return render(request, 'platform.html')

def in_games(request):
    return render(request, 'games.html')

def in_cart(request):
    return render(request, 'cart.html')