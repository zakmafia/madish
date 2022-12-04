from django import forms
from django.forms import ModelForm
from .models import FoodMenu

class FoodMenuForm(ModelForm):
    image = forms.ImageField()
    class Meta:
        model = FoodMenu
        fields = ['name', 'image', 'detail', 'price']

        def __init__(self, *args, **kwargs):
            super(FoodMenuForm, self).__init__(*args, **kwargs)
            self.fields['name'].widget.attrs['placeholder'] = 'Enter the name'
            self.fields['detail'].widget.attrs['placeholder'] = 'Enter the detail'
            self.fields['price'].widget.attrs['placeholder'] = 'Enter the price'
            for field in self.fields:
                self.fields[field].widget.attrs['class'] = 'form-control'
