from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Carreras, Alumnos
from .forms import CrearCarrera

# Create your views here.
def hola(request):
    return HttpResponse("<h1>Hola Luis al mundo Django</h1><br><a href='saludo2' >IR A DEMO</a>")

def demo(request):
    return HttpResponse("<h1>Demo 1</h1><br><a href='saludo' >Regresar</a>")

def consultar_carreras(request):
    carreras = list(Carreras.objects.values())
    return JsonResponse(carreras,safe=False)

def ver_alumno(request,id_alu):
    a = Alumnos.objects.get(id=id_alu)
    return HttpResponse('Datos del Alumno: <br>No. Ctrol:%s<br>Nombre: %s %s %s <br>Carrera %s' % (a.no_ctrol,a.nombre,a.ap_pat,a.ap_mat,a.carrera.nombre))

def index(request):
    return render(request, 'index.html')

def carreras(request):
    carr = Carreras.objects.all()
    return render(request,'carreras.html',{
        'carreras' : carr
    })

def alumnos(request):
    alu = Alumnos.objects.all()
    return render(request,'alumnos.html',{
        'alumnos': alu
    })

def create_carrera(request):
    return render(request,'carreras/create.html',{
        'formulario': CrearCarrera()
    })

def insert_carrera(request):
    Carreras.objects.create(nombre=request.POST['nombre1'],status=request.POST['status1'])
    return redirect('/alumnos/carreras')