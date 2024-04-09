from django.db import models

# Create your models here.
class Newreg(models.Model):
    name = models.CharField(max_length=30)
    Gmail = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    fathername = models.CharField(max_length=30)
    date = models.DateField()