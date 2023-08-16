from django import forms
from .models import Entregable, Profesor, Estudiante, Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

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

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields 