from django.shortcuts import render

# Create your views here.


def in_platform(request):
    return render(request, 'platform.html')

def in_games(request):
    games = ['Atomic Heart', 'Cyberpunk 2077']
    game2 = 'PayDay 2'
    context = {
        'games1': games,
        'games2': game2
    }
    return render(request, 'games.html', context)

def in_cart(request):
    return render(request, 'cart.html')