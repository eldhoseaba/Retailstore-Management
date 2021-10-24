from django.db import models

# Create your models here.
class prdct(models.Model):
	Name=models.CharField(max_length=20)
	Category=models.CharField(max_length=20)
	Price=models.IntegerField()
	Image=models.ImageField(upload_to=None)