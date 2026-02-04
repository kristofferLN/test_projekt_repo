from django.contrib import admin
from .models import Bruger
# Register your models here.

@admin.register(Bruger)
class BrugerAdmin(admin.ModelAdmin):
    list_display = ('id', 'brugernavn', 'email')
    search_fields = ('brugernavn', 'email')
    list_display_links = ('id', 'brugernavn')

# Register your models here.
