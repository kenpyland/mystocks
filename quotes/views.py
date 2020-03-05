from django.shortcuts import render, redirect
from .models import Mystockdb
from .forms import StockForm
from django.contrib import messages

# 
#  API Token: pk_991513add74a484d9ad2ef036d1c20c3 


def home(request):
	import requests 
	import json

	

	if request.method == 'POST':
		ticker = request.POST['ticker']
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_991513add74a484d9ad2ef036d1c20c3")

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error"
		return render(request, 'home.html', {'api': api, 'ticker': ticker})


	else:	
		return render(request, 'home.html', {'ticker': "Enter a symbol to search"})

	
	

def about(request):
	return render(request, 'about.html', {})

def add_mystocks(request):
	import requests
	import json

	# request to add something to the database 

	if request.method == 'POST':
		form = StockForm(request.POST or None)
		
		if form.is_valid():		
			form.save()	
			messages.success(request, ("Stock Was Added"))
			return redirect('add_mystocks')

	# else we will display the database

	else:	
		allstocks = Mystockdb.objects.all()                               # get everything out of the db



		context = {'allstocks': allstocks}                                 
		return render(request, 'add_mystocks.html', context)

def delete(request, db_pkey):		
	item = Mystockdb.objects.get(pk=db_pkey)
	item.delete()
	messages.success(request, ("Stock Was deleted"))
	return redirect('add_mystocks')