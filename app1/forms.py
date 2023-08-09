from django import forms
from .models import Entregable, Profesor, Estudiante

class EntregableForm(forms.ModelForm):
    class Meta:
        model = Entregable
        fields = '__all__'

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'

class CursoSearchForm(forms.Form):
    nombre = forms.CharField(required=False)