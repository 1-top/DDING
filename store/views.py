from django.shortcuts import render

# Create your views here.
from DDING.settings import get_secret
from store.models import Report


def home(request):
    return render(request, 'main.html')


def dding(request):
    SECRET_KEY = get_secret('KAKAO')

    if request.method == 'POST':
        category = request.POST.get('category', None)
        location = request.POST.get('location', None)
        storename = request.POST.get('storename', None)
        latitude = request.POST.get('latitude', None)
        longitude = request.POST.get('longitude', None)
        print(category, location, storename, latitude, longitude)

    return render(request, 'dding.html', {'key': SECRET_KEY})
