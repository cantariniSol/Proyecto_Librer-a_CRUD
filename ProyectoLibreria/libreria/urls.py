from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static 

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'), 
    path('libros/', views.libros, name='libros'),
    path('libros/crear_libros/', views.crear_libros, name='crear_libros'),
    path('libros/editar_libro/<int:id>', views.editar_libro, name='editar_libro'),
    path('eliminar/<int:id>', views.eliminar_libro, name='eliminar_libro'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )