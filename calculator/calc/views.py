from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	#return HttpResponse("<h1>Hello World</h1>")
	return render(request,'calculator.html')
#def display(request):
	#name=request.GET["txt1"]
	#return render(request,"example.html",{"msg":"welcome"+""+name})
#def add(request):
	#num1=int(request.GET["txt1"])
	#num2=int(request.GET["txt2"])
	#return render(request,"example.html",{"msg":num1+num2})
def result(request):
	num1=int(request.POST["txt1"])
	num2=int(request.POST["txt2"])
	if(request.POST["btn1"]=="+"):
		result=num1+num2
		return render(request,"calculator.html",{"msg":result})
	elif(request.POST["btn1"]=="-"):
		result=num1-num2
		return render(request,"calculator.html",{"msg":result})
	elif(request.POST["btn1"]=="*"):
		result=num1*num2
		return render(request,"calculator.html",{"msg":result})
	elif(request.POST["btn1"]=="/"):
		result=num1/num2
		return render(request,"calculator.html",{"msg":result})
	else:
		result=num1%num2
		return render(request,"calculator.html",{"msg":result})
	
