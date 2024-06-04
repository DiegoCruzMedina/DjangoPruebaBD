from django.shortcuts import render
from .models import Genero,alumno
# Create your views here.

def index(request):
    alumnos = alumno.objects.all() #Select * FROM
    context = {"alumnos":alumnos}
    return render(request,"alumnos/index.html",context)

def index2(request):
    alumnos = alumno.objects.raw("SELECT * FROM alumnos_alumno") #Select * FROM
    context = {"alumnos":alumnos}
    return render(request,"alumnos/listadoSQL.html",context)
