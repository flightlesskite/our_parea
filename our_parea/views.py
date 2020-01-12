from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'our_parea/index.html', {})

def food(request):
    return render(request, 'our_parea/food.html', {})

def culture(request):
    return render(request, 'our_parea/culture.html', {})
