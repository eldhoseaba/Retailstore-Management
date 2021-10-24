from django.db import models

# Create your models here.
class expenses(models.Model):
	Name=models.CharField(max_length=20)
	Amount=models.IntegerField()


class balances(models.Model):
	Amount=models.IntegerField()