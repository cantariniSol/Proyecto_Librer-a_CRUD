from dataclasses import field, fields
from django import forms
from .models import Libros

class LibroForm(forms.ModelForm):
    
    class Meta:
        model = Libros
        fields =['id', 'titulo', 'imagen', 'descripcion']