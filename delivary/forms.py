from django import forms # type: ignore

from .models import Menu, Restaurants


class ResForm(forms.ModelForm):
    class Meta:
        model=Restaurants
        fields = ['res_name','food_cat','rating','img','address']


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['res','item_name', 'description', 'price', 'is_available', 'category']