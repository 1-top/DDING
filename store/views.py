from django.shortcuts import render

# Create your views here.
from DDING.settings import get_secret
from store.models import Report, Category


def home(request):
    return render(request, 'main.html')


def dding(request):
    SECRET_KEY = get_secret('KAKAO')

    if request.method == 'POST':
        _category = request.POST.get('category', None)
        location = request.POST.get('location', None)
        storename = request.POST.get('storename', None)
        latitude = request.POST.get('latitude', None)
        longitude = request.POST.get('longitude', None)
        category, _ = Category.objects.get_or_create(name=_category)
        if category and location and storename and latitude and longitude:
            Report(category=category, location=location, name=storename, latitude=latitude, longitude=longitude).save()

    return render(request, 'dding.html', {'key': SECRET_KEY})
