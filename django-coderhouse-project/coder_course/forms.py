from django import forms

class cargarFamilia(forms.Form):
    codigo= forms.CharField()
    nombre=forms.CharField()
    label = "Familia"
   


class cargarRubro(forms.Form):
    codigo= forms.CharField()
    nombre=forms.CharField()
    label = "Rubros"
      
class cargarTarea(forms.Form):
    codigo = forms.CharField()
    rubro = forms.CharField()
    tarea = forms.CharField()
    unidad = forms.CharField()
    costo = forms.IntegerField()
    fecha = forms.DateField()
    especificacion = forms.CharField()
