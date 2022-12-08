from django import forms
from shop import models
from .models import CustomerSupport

class clienteForm(forms.ModelForm):
    class Meta:
        model = CustomerSupport
        fields = ['content']

class buscador_productos(forms.Form):
    producto = forms.CharField(required=False)