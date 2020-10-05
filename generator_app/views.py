from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import random


def home(request):
    return render(request, 'generator_app/home.html')


def generator(request):
    CHARACTERS = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length', 12))

    if request.GET.get('Uppercase'):
        CHARACTERS.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('Numeric'):
        CHARACTERS.extend(list('0123456789'))
    if request.GET.get('Special'):
        CHARACTERS.extend(list('!@#$%^&*()'))

    createdPassword = ''

    for _ in range(length):
        createdPassword += random.choice(CHARACTERS)

    return render(request, 'generator_app/password.html', {'password': createdPassword})


def about(request):
    return render(request, 'generator_app/about.html')
