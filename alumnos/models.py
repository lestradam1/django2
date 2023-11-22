from django.db import models

# Create your models here.
class Carreras(models.Model):
    nombre = models.CharField(max_length=80)
    status = models.SmallIntegerField()

    def __str__(self):
        return self.nombre

class Alumnos(models.Model):
    no_ctrol = models.CharField(max_length=20)
    nombre = models.CharField(max_length=80)
    ap_pat = models.CharField(max_length=80)
    ap_mat = models.CharField(max_length=80)
    carrera = models.ForeignKey(Carreras,on_delete=models.PROTECT)
    #carrera = models.ForeignKey(Carreras, on_delete=models.CASCADE)
    status = models.SmallIntegerField()

    def __str__(self):
        return self.nombre