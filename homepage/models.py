from django.db import models

# Create your models here.

class contactdata(models.Model):
    name=models.CharField(max_length=100)
    emailid=models.CharField(max_length=100)
    msg=models.TextField()