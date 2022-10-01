from django.db import models
from .historia_clinica import Historia_clinica


class Signos_vitales(models.Model):
    id_signos_vitales= models.AutoField(primary_key=True)
    Hora_signo_vital = models.TimeField()
    Oximetria = models.CharField('Oximetria', max_length=20)
    Frecuencia_respiratoria = models.CharField('Frecuencia respiratoria', max_length=20)
    Frecuencia_cardiaca = models.CharField('Frecuencia respiratoria', max_length=20)
    Temperatura= models.CharField('Temperatura', max_length=20)
    Presion_arterial= models.CharField('Presion arterial', max_length=20)
    Glucemias= models.CharField('Glucemias', max_length=20)
    id_historia_clinica= models.ForeignKey(Historia_clinica,related_name='signos_vitales',on_delete=models.CASCADE)
    