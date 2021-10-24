from django.db import models

# Create your models here.
class phnbook(models.Model):
	Name=models.CharField(max_length=20)
	Phno=models.IntegerField()