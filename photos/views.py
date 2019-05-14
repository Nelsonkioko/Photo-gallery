from django.shortcuts import render
from .models import Image, Location, Category
from django.views.generic import ListView


def home(request):
    context = {
        'images': Image.objects.all()
    }
    return render(request, 'photos/home.html', context)


class PicListView(ListView):
    model = Image
    template_name = 'photos/home.html'
    context_object_name = "images"


def GetLocation(request):
    data = request.GET["Location"]
    locale = Location.objects.filter(image_location=data).first()
    categ = Category.objects.filter(image_category=data).first()
    if locale:
        images = Image.objects.filter(image_location=locale)
    elif categ:
        images = Image.objects.filter(image_category=categ)
    else:
        images = {}
    return render(request, 'location.html', {"images": images})
