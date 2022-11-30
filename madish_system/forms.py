from django import forms
from django.forms import ModelForm
from .models import FoodMenu, Size, Extra

class FoodMenuForm(ModelForm):
    image = forms.ImageField()
    class Meta:
        model = FoodMenu
        fields = ['name', 'image', 'detail', 'price', 'has_size']

        def __init__(self, *args, **kwargs):
            super(FoodMenuForm, self).__init__(*args, **kwargs)
            self.fields['name'].widget.attrs['placeholder'] = 'Enter the name'
            self.fields['detail'].widget.attrs['placeholder'] = 'Enter the detail'
            self.fields['price'].widget.attrs['placeholder'] = 'Enter the price'
            for field in self.fields:
                self.fields[field].widget.attrs['class'] = 'form-control'

        
class ExtraForm(ModelForm):
    class Meta:
        model = Extra
        fields = ['name',]

    def __init__(self, *args, **kwargs):
        super(ExtraForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Enter the name'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class SizeForm(ModelForm):
    class Meta:
        model = Size
        fields = ['size',]

    def __init__(self, *args, **kwargs):
        super(SizeForm, self).__init__(*args, **kwargs)
        self.fields['size'].widget.attrs['placeholder'] = 'Enter the size'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'