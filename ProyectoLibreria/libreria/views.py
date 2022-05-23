from django.shortcuts import render, redirect
from .models import Libros
from .forms import LibroForm
# Create your views here.

# Accesos a las distintas paginas
def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

#Acceso a las funciones de libro
def libros(request):
    libros = Libros.objects.all();
    #print(libros) --> Devuelve una lista de libros
    return render(request, 'libros/index.html', {'libros': libros})

def crear_libros(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    
    return render(request, 'libros/crear.html', {'formulario': formulario})

def editar_libro(request, id):
    libro = Libros.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    
    if formulario.is_valid() and request.POST: #PUEDE SER TAMBIÉN request.method == 'POST'
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/editar.html', {'formulario': formulario})

def eliminar_libro(request, id):
    libro = Libros.objects.get(id=id)
    libro.delete()
    return redirect('libros')
