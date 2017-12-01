from django.forms import ModelForm

from question1.models import OpeningStock

class OpeningStockForm(ModelForm):
	class Meta:
		model = OpeningStock
		fields = ["miti","quantity","value","specification","remarks"]