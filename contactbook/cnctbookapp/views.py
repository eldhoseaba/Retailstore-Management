from django.shortcuts import render
from django.http import HttpResponse
from .models import phnbook

# Create your views here.
def home(request):
	return render(request,'phonebook.html')


flag=0
def add(request):
	responseDic={}
	try:
		name=request.POST['txt1']
		phno=request.POST['txt2']
		cntlist=phnbook.objects.all()
		for i in cntlist:
			if name in i.Name:
				responseDic["msg"]="Already exists"
				return render(request,"phonebook.html",responseDic)
			
		cnlist=phnbook(Name=name,Phno=phno)
		cnlist.save()
		responseDic["msg1"]="Contact added"
		return render(request,"phonebook.html",responseDic)
	except Exception as e:
		print(e)
		responseDic["msg2"]="Contact cannot be added"
		return render(request,"phonebook.html",responseDic)
	

def delete(request):
	responseDic={}
	try:
		name=request.POST['txt1']
		cnlist=phnbook.objects.get(Name=name)
		cnlist.delete()
		responseDic["msg12"]="Deleted successfully"
		return render(request,"phonebook.html",responseDic)
	except Exception as e:
		print(e)
		responseDic["msg123"]="Delete unsuccessfull"
		return render(request,"phonebook.html",responseDic)


def Nameupdation(request):
	responseDic={}
	try:

		old=request.POST['txt1']
		new=request.POST['txt2']
		cntlist=phnbook.objects.all()
		for i in cntlist:
			if(new in i.Name):
				responseDic["msg121"]="Already exists"
				return render(request,"phonebook.html",responseDic)
	
		cntlist=phnbook.objects.get(Name=old)
		cntlist.Name=new
		cntlist.save()
		responseDic["msg21"]="Updated successfully"
		return render(request,"phonebook.html",responseDic)
	except Exception as e:
		print(e)
		responseDic["msg22"]="Update unsuccessfull"
		return render(request,"phonebook.html",responseDic)		
def PhNoupdation(request):
	responseDic={}
	try:

		name=request.POST['txt1']
		phno=request.POST['txt2']
		cntlist=phnbook.objects.get(Name=name)
		cntlist.Phno=phno
		cntlist.save()
		responseDic["msg21"]="Updated successfully"
		return render(request,"phonebook.html",responseDic)
	except Exception as e:
		print(e)
		responseDic["msg22"]="Update unsuccessfull"
		return render(request,"phonebook.html",responseDic)





def display(request):
	cntlist=phnbook.objects.all()
	return render(request,"phonebook.html",{'cntlist':cntlist})