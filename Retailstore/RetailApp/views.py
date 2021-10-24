from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from .models import product,customer,company,order,sales,cart
# Create your views here.
@login_required
def home(request):
	#return HttpResponse("<h1>Hello World</h1>")
	#return render(request,'homepage.html')
	return render(request,'homepage.html')
	#return render(request,'customer.html')
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

@login_required
def addproduct(request):
	responseDic={}
	try:
		prdct=request.POST['Prdtname']
		types=request.POST['types']
		company=request.POST['cmpny']
		price=request.POST['price']
		stock=request.POST['stock']
		pdlist=product(Product_Name=prdct,Type=types,Company=company,Price=price,Stock=stock)
		pdlist.save()
		responseDic["msg1"]="Product added"
		return render(request,"product.html",responseDic)
	except Exception as e:
		print(e)
		responseDic["msg2"]="Product cannot be added"
		return render(request,"product.html",responseDic)
	
@login_required
def addcustomer(request):
	responseDic={}
	try:
		cust=request.POST['csname']
		contact=request.POST['cnct']
		cslist=customer(Customer_Name=cust,Contact=contact)
		cslist.save()
		responseDic["msg11"]="customer added"
		return render(request,"product.html",responseDic)
	except Exception as e:
		print(e)
		responseDic["msg12"]="customer cannot be added"
		return render(request,"customer.html",responseDic)

@login_required	
def addcmpny(request):
	responseDic={}
	try:
		cname=request.POST['cmpny']
		cmplist=company(Company=cname)
		cmplist.save()
		responseDic["msgaa"]="company added"
		return render(request,"company.html",responseDic)
	except Exception as e:
		print(e)
		responseDic["msgbb"]="company cannot be added"
		return render(request,"company.html",responseDic)

@login_required		
def orderprdct(request):
	responseDic={}
	try:
		cname=request.POST['csname']
		prdct=request.POST['ps']
		types=request.POST['tp']
		company=request.POST['cmp']
		price=request.POST['pr']
		qt=request.POST['qn']
		odlist=order(Customer_Name=cname,Product_Name=prdct,Type=types,Company=company,Quantity=qt,Price=price)
		odlist.save()
		responseDic["msg1"]="added"
		return render(request,"order.html",responseDic)
	except Exception as e:
		print(e)
		responseDic["msg2"]="cannot be added"
		return render(request,"order.html",responseDic)
	
@login_required
def addsales(request):
	responseDic={}
	try:
		cname=request.POST['csname']
		cnct=request.POST['cnct']
		date=request.POST['dt']
		cslist=order.objects.all()
		flag=0
		tp=0
		for i in cslist:
			if cname in i.Customer_Name:
				flag=1
		if(flag==1):
			cslist=order.objects.get(Customer_Name=cname)
			tp=cslist.Price
			sllist=sales(Customer_Name=cname,Contact=cnct,Date=date,Total=tp)
			sllist.save()
		responseDic["msg1a"]="added"
		return render(request,"sales.html",responseDic)
	except Exception as e:
		print(e)
		responseDic["msg2a"]="cannot be added"
		return render(request,"sales.html",responseDic)
	
@login_required
def addcart(request):
	responseDic={}
	try:
		cname=request.POST['cstname']
		prdct=request.POST['pds']
		types=request.POST['tps']
		company=request.POST['cmpy']
		price=request.POST['prc']
		qt=request.POST['qnt']
		cslist=order.objects.all()
		flag=0
		tp=0
		for i in cslist:
			if cname in i.Customer_Name:
				flag=1
		if(flag==1):
			cslist=order.objects.get(Customer_Name=cname)
			ctlist=cart(Product_Name=prdct,Type=types,Company=company,Quantity=qt,Price=price)
			ctlist.save()
		responseDic["msga11"]="added"
		return render(request,"cart.html",responseDic)
	except Exception as e:
		print(e)
		responseDic["msga22"]="cannot be added"
		return render(request,"cart.html",responseDic)

def displaycart(request):
	cslist=cart.objects.all()
	return render(request,"displaycart.html",{'cslist':cslist})


def displayorder(request):
	odlist=order.objects.all()
	return render(request,"Vieworder.html",{'odlist':odlist})

def displayproduct(request):
	pdlist=product.objects.all()
	return render(request,"Viewproduct.html",{'pdlist':pdlist})


def displaysales(request):
	sllist=sales.objects.all()
	return render(request,"viewsales.html",{'sllist':sllist})