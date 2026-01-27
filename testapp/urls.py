from django.urls import path
from . import views

urlpatterns = [path('about/', views.homeAbout_view),
               path('', views.home_view) ]