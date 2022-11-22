from django import forms

class clienteForm(forms.Form):
    tipo_de_consulta = forms.ChoiceField(choices=[('pregunta','Pregunta'),
          ('recomendacion','Recomendacion'),('reclamacion','Reclamacion'),('otro','Otro')])
    pregunta = forms.CharField()
    descripcion = forms.CharField()