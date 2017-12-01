from django.forms import ModelForm
from django import forms
from .models import Item

from question1.models import OpeningStock

class OpeningStockForm(ModelForm):

	item = forms.CharField(
    	widget=forms.Select(
        	choices=Item.objects.all().values_list('id', 'name')
        )
    )
    
	class Meta:
		model = OpeningStock
		fields = ["item","miti","quantity","value","specification","remarks"]