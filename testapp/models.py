from django.db import models

# Create your models here.
class Bruger(models.Model):
    brugernavn = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)