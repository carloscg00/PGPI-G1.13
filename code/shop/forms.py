from django import forms
from shop import models

class clienteForm(forms.Form):
    content = forms.CharField(required=True)

class buscador_productos(forms.Form):
    producto = forms.CharField(required=False)