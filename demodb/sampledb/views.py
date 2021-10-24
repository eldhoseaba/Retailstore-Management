from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from .models import employee
# Create your views here.
@login_required
def home(request):
	#return HttpResponse("<h1>Hello World</h1>")
	return render(request,'employee.html')
	#return render(request,'sample.html')
#def display(request):
	#name=request.GET["txt1"]
	#return render(request,"example.html",{"msg":"welcome"+""+name})
#def add(request):
	#num1=int(request.GET["txt1"])
	#num2=int(request.GET["txt2"])
	#return render(request,"example.html",{"msg":num1+num2})
@login_required	
def add(request):
	responseDic={}
	try:
		name=request.POST['txt1']
		address=request.POST['txt2']
		emplist=employee(Name=name,Address=address)
		emplist.save()
		responseDic["msg1"]="Employee added"
		return render(request,"employee.html",responseDic)
	except Exception as e:
		print(e)
		responseDic["msg2"]="Employee cannot be added"
		return render(request,"employee.html",responseDic)
	
		
# Create your views here.
def display(request):
	empdtls=employee.objects.all()
	return render(request,"employee.html",{'empdtls':empdtls})
	#empdtls=employee.objects.get(id='5')
	#empdtls.Name,empdtls.Address
	#return render(request,"employee.html",{'empdtls':empdtls})
@login_required
def delete(request):
	responseDic={}
	try:
		name=request.POST['txt1']
		emplist=employee.objects.filter(Name=name)
		emplist.delete()
		responseDic["msg12"]="Deleted successfully"
		return render(request,"employee.html",responseDic)
	except Exception as e:
		print(e)
		responseDic["msg123"]="Delete unsuccessfull"
		return render(request,"employee.html",responseDic)



@login_required
def update(request):
	responseDic={}
	try:
		name=request.POST['txt1']
		address=request.POST['txt2']
		emplist=employee.objects.get(Name=name)
		emplist.Address=address
		emplist.save()
		responseDic["msg21"]="Updated successfully"
		return render(request,"employee.html",responseDic)
	except Exception as e:
		print(e)
		responseDic["msg22"]="Update unsuccessfull"
		return render(request,"employee.html",responseDic)



def loginview(request):
	username=request.POST['username']
	password=request.POST['password']
	user=authenticate(request,username=username,password=password)
	if user is not None:
		login(request,user)
		return redirect('/')
	else:
		return render(request,"login.html")


def logout_view(request):
	logout(request)
	return redirect('/',{'msg':"invalid login"})



def sign_up(request):
	dic1={}
	form=UserCreationForm(request.POST)
	if(request.method)=="POST":
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			password=form.cleaned_data.get('password1')
			user=authenticate(request,username=username,password=password)
			login(request,user)
			return redirect("login")
	else:
		form=UserCreationForm()
	return render(request,'registration/signup.html',{'form':form})

	
