from django.shortcuts import render
from.models import Image
def home(request):
   context = {
       'images': Image.objects.all()
   }
   return render(request, 'photos/home.html', context)
