from django.db import models

# Create your models here.
class company(models.Model):
	Company=models.CharField(max_length=20)

class customer(models.Model):
	Customer_Name=models.CharField(max_length=20)
	Contact=models.IntegerField()	

class product(models.Model):
	Product_Name=models.CharField(max_length=20)
	Type=models.CharField(max_length=20)
	Company=models.CharField(max_length=20)
	Price=models.IntegerField()
	Stock=models.CharField(max_length=20)

class sales(models.Model):
	Customer_Name=models.CharField(max_length=20)
	Contact=models.IntegerField()
	Date=models.DateTimeField()
	Total=models.IntegerField()
class order(models.Model):
	Customer_Name=models.CharField(max_length=20)
	Product_Name=models.CharField(max_length=20)
	Type=models.CharField(max_length=20)
	Company=models.CharField(max_length=20)
	Quantity=models.IntegerField()
	Price=models.IntegerField()

class cart(models.Model):
	Product_Name=models.CharField(max_length=20)
	Type=models.CharField(max_length=20)
	Company=models.CharField(max_length=20)
	Quantity=models.IntegerField()
	Price=models.IntegerField()



		