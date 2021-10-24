from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	#return HttpResponse("<h1>Hello World</h1>")
	return render(request,'vote.html')
#def display(request):
	#name=request.GET["txt1"]
	#return render(request,"example.html",{"msg":"welcome"+""+name})
#def add(request):
	#num1=int(request.GET["txt1"])
	#num2=int(request.GET["txt2"])
	#return render(request,"example.html",{"msg":num1+num2})
def result(request):
	name=request.GET["txt1"]
	age=int(request.GET["txt2"])
	if(age>18):
		return render(request,"result.html",{"msg":name+" "+"you are eligible"})
	else:
		return render(request,"result.html",{"msg":name+" "+"you are not eligible"})