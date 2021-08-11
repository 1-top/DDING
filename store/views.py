from django.shortcuts import render

# Create your views here.
from DDING.settings import get_secret


def home(request):
    return render(request, 'main.html')


def dding(request):
    if request.method == 'GET':
        SECRET_KEY = get_secret('KAKAO')
    elif request.method == 'POST':
        pass
    return render(request, 'dding.html', {'key': SECRET_KEY})
