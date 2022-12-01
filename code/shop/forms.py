from django import forms
from shop import models

class clienteForm(forms.Form):
    sugerencia = forms.CharField(required=True)

class reservaForm(forms.Form):
      servicio =  forms.ChoiceField(choices=[('corte_caballero','Corte para caballero'),
          ('corte_niño','Corte para niño'),('arreglo_barba','Barba'),('tinte','Tinte')])  
      informacion_extra = forms.CharField()

class buscador_productos(forms.Form):
    producto = forms.CharField(required=False)