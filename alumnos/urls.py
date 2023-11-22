from django.urls import path
from . import views

urlpatterns = [
    path('saludo',views.hola),
    path('',views.index),
    path('saludo2',views.demo),
    path('ver_carreras',views.consultar_carreras),
    path('ver_alumno/<int:id_alu>',views.ver_alumno),
    path('index',views.index),
    path('carreras',views.carreras),
    path('alumnos',views.alumnos),
    
    path('create_carrera',views.create_carrera),
    path('insert_carrera',views.insert_carrera),
]