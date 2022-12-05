from django import forms
from django.forms import ModelForm
from .models import FoodMenu, Category

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the name'})
        }


class FoodMenuForm(ModelForm):
    image = forms.ImageField()
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple()
        )
    class Meta:
        model = FoodMenu
        fields = ['name', 'image', 'detail', 'price', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the name'}),
            'detail': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the detail'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the price'}),
        }
