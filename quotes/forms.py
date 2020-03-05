from django import forms
from .models import Mystockdb

class StockForm(forms.ModelForm):
	class Meta:
		model = Mystockdb
		fields = ["myticker", 'myprice', "myowned"]