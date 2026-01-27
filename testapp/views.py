from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def base_url_view(request):
    return HttpResponse("hey base_url")

def home_view(request):
    return HttpResponse("hey home")

def homeAbout_view(request):
    return HttpResponse("hey homeAbout")