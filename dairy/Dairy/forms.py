from django import forms
from models import Farmer

class FarmerForm(forms.ModelForm):
	
	class Meta:
		model=Farmer
