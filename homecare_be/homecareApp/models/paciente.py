from django.db import models
from .usuario import Usuario
from .familiar import Familiar
from .personal_medico import Personal_medico


class Paciente(models.Model):
    id_Paciente= models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=35)
    apellidos = models.CharField('Apellidos', max_length=35)
    telefono  = models.CharField('Telefono', max_length=35)
    genero = models.CharField('Genero', max_length=35)
    direccion = models.CharField('Direccion', max_length=100)
    ciudad = models.CharField('Ciudad', max_length=35)
    correo = models.CharField('Correo', max_length=100)
    fecha_nacimiento= models.DateField()
    id_familiar= models.ForeignKey(Familiar,related_name='paciente',on_delete=models.CASCADE)
    id_personal_medico= models.ForeignKey(Personal_medico,related_name='paciente',on_delete=models.CASCADE)
    id_Usuario= models.ForeignKey(Usuario,related_name='paciente',on_delete=models.CASCADE)