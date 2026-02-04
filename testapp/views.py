from django.shortcuts import render
from django.http import HttpResponse
from .models import Bruger


# Create your views here.
def base_url_view(request):
    return HttpResponse("hey base_urlen")

def home_view(request):
    return HttpResponse("hey home")

def homeAbout_view(request):
    database_data = Bruger.objects.all()
    print(database_data)
    return render(request, "homeAbout.html", {"database": database_data})