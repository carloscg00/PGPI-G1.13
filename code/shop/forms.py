from django import forms

class clienteForm(forms.Form):
    tipo_de_consulta = forms.ChoiceField(choices=[('pregunta','Pregunta'),
          ('recomendacion','Recomendacion'),('reclamacion','Reclamacion'),('otro','Otro')])
    pregunta = forms.CharField()
    descripcion = forms.CharField()


class reservaForm(forms.Form):
      servicio =  forms.ChoiceField(choices=[('corte_caballero','Corte para caballero'),
          ('corte_niño','Corte para niño'),('arreglo_barba','Barba'),('tinte','Tinte')])  
      informacion_extra = forms.CharField()

class buscador_productos(forms.Form):
    producto = forms.CharField(required=False)