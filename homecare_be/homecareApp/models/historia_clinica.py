from django.db import models
from .paciente import Paciente
from .familiar import Familiar
from .personal_medico import Personal_medico


class Historia_clinica(models.Model):
    id_haclinica= models.AutoField(primary_key=True)
    diagnostico = models.CharField('Diagnostico', max_length=200)
    entorno = models.CharField('Entorno', max_length=200)
    fecha_entorno  = models.DateField()
    Sugerencias = models.CharField('Genero', max_length=200)
    fecha_sugerencias = models.DateField()
    id_familiar= models.ForeignKey(Familiar,related_name='historia_clinica',on_delete=models.CASCADE)
    id_personal_medico= models.ForeignKey(Personal_medico,related_name='historia_clinica',on_delete=models.CASCADE)
    id_paciente= models.ForeignKey(Paciente,related_name='historia_clinica',on_delete=models.CASCADE)