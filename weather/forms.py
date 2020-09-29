from django.forms import ModelForm, TextInput
from .models import City


class CityForm(ModelForm):
    
    class Meta:
        model = City
        fields = ['name',]
    
    def clean(self): 
    	cleaned_data=super(CityForm,self).clean()
    	return cleaned_data

    	



    
    