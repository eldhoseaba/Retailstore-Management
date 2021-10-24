from django.db import models

# Create your models here.
class employee(models.Model):
	Name=models.CharField(max_length=20)
	Address=models.CharField(max_length=20)