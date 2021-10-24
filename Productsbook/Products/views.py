from django.shortcuts import render
from django.http import HttpResponse
from .models import prdct
def search(request):
	#return HttpResponse("<h1>Hello World</h1>")
	#return render(request,'homepage.html')
	allprods={}
	catprods=prdct.objects.values('Category','id')
	cats={item['Category'] for item in catprods}
	for cat in cats:
		prod=prdct.objects.filter(Category=cat)
	return render(request,"homepage.html",{'allprods':prod})
#ab=prdct.objects.values('Name','id').order_by('-check_in')


	#return render(request,'product.html')


def addproduct(request):
	responseDic={}
	try:
		pro=request.POST['Prdtname']
		cate=request.POST['cmpny']
		price=request.POST['price']
		img=request.POST['stock']
		pdlist=prdct(Name=pro,Category=cate,Price=price,Image=img)
		pdlist.save()
		responseDic["msg1"]="Product added"
		return render(request,"product.html",responseDic)
	except Exception as e:
		print(e)
		responseDic["msg2"]="Product cannot be added"
		return render(request,"product.html",responseDic)
	