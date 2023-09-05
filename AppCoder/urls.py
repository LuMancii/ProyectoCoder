from django.urls import path
from .views import curso, lista_cursos, inicio, cursos, profesores, estudiantes, entregables

urlpatterns = [
    path('curso-nuevo/<nombre>/<camada>', curso),
    path('lista-cursos/', lista_cursos),
    path('', inicio, name = 'Inicio'),
    path('cursos/', cursos, name= 'Cursos'),
    path('profesores/', profesores, name= 'Profesores'),
    path('estudiantes/', estudiantes, name ='Estudiantes'),
    path('entregables/', entregables, name = 'Entregables'),
    ]
