from django.shortcuts import render
from django.http import HttpResponse
from .models import expenses
from .models import balances
# Create your views here.
def home(request):
	return render(request,'expensetracker.html')

	

amt=0	
cb=0	
def add(request):
	responseDic={}
	try:
		name=request.POST['txt1']
		amount=int(request.POST['txt2'])
		bln=balances.objects.get(id=1)
		if int(amount)>bln.Amount:
			responseDic["msg"]="Insufficient balance"
			return render(request,"expensetracker.html",responseDic)
		else:	
			flag=0 
			explist=expenses.objects.all()
			for i in explist:
				if name in i.Name:
					flag=1	
			if(flag==1):
				explist=expenses.objects.get(Name=name)
				amt=explist.Amount+amount
				explist.Amount=amt
				explist.save()
				blnlist=balances.objects.get(id=1)
				cb=blnlist.Amount-amount
				blnlist.Amount=cb
				blnlist.save()
				print(blnlist.Amount)	
				responseDic["msg1"]="Expense added and Balance updated"
				return render(request,"expensetracker.html",responseDic)	
			else:
				explist=expenses.objects.all()
				explist=expenses(Name=name,Amount=amount)
				explist.save()
				blnlist=balances.objects.get(id=1)
				cb=blnlist.Amount-amount
				blnlist.Amount=cb
				blnlist.save()
				print(blnlist.Amount)
				responseDic["msg1"]="Expense added and Balance updated"
				return render(request,"expensetracker.html",responseDic)
				
		
	except Exception as e:
		print(e)
		responseDic["msg2"]="Expense cannot be added"
		return render(request,"expensetracker.html",responseDic)		
		
	
def display(request):
	explist=expenses.objects.all()
	return render(request,"expensetracker.html",{'explist':explist})
def display2(request):
	bln=balances.objects.get(id=1)
	return render(request,"expensetracker.html",{'bln':bln})



def update(request):
	responseDic={}
	try:
		amount=int(request.POST['txt1'])
		bln=balances.objects.get(id=1)
		amt=bln.Amount+amount
		bln.Amount=amt
		bln.save()
		responseDic["msg12"]="Balance added"
		return render(request,"expensetracker.html",responseDic)
	except Exception as e:
		print(e)
		responseDic["msg123"]="Balance cannot be added"
		return render(request,"expensetracker.html",responseDic)			