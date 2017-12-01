from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

import json
from .models import OpeningStock
from django.http import HttpResponse
from .forms import  OpeningStockForm
from dateutil import parser

def index(request):

	form = OpeningStockForm(request.POST or None)
	if request.method == "POST":

		# manually retrieve fields and create object
		data = request.POST
		date = parser.parse(data['date'])
		data['quantity']
		data['value'] 
		data['specification']
		data['remarks'] 

		s = OpeningStock(miti=date, quantity=data['quantity'], value=data['value'], specification=data['specification'], remarks=data['remarks'])
		s.save()		
		
		return HttpResponse(json.dumps({'result': 'success', 'data': request.POST}))
	else:
		context = {}
		context['form'] = form		
		return render(request, 'question1/index.html', context)
