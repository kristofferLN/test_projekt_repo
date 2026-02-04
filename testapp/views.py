from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def base_url_view(request):
    return HttpResponse("hey base_urlen")

def home_view(request):
    return HttpResponse("hey home")

def homeAbout_view(request):
    return render(request, "homeAbout.html", {"pladsholder_navn": "pladsholder_indhold"})