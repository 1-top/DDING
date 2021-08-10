from django.shortcuts import render

# Create your views here.
from DDING.settings import get_secret


def home(request):
    return render(request, 'main.html')


def dding(request):
    SECRET_KEY = get_secret('KAKAO')
    return render(request, 'dding.html', {'key': SECRET_KEY})
