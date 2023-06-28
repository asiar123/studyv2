from django.db import models
from user.models import Usuario

# Create your models here.

class matery(models.Model):
	user=models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)
	Nombre = models.CharField(max_length=100, null=True)
	Orientacion1 = models.CharField(max_length=100, null=True)
	Orientacion2 = models.CharField(max_length=100, null=True)
	Orientacion3 = models.CharField(max_length=100, null=True)
	Orientacion4 = models.CharField(max_length=100, null=True)
	Orientacion5 = models.CharField(max_length=100, null=True)
	Espacial1 = models.CharField(max_length=100, null=True)
	Espacial2 = models.CharField(max_length=100, null=True)
	Espacial3 = models.CharField(max_length=100, null=True)
	Espacial4 = models.CharField(max_length=100, null=True)
	Espacial5 = models.CharField(max_length=100, null=True)
	fijacion = models.CharField(max_length=100, null=True)
	calculo = models.CharField(max_length=100, null=True)
	recuerdo = models.CharField(max_length=100, null=True)
	lenguaje1 = models.CharField(max_length=100, null=True)
	lenguaje2 = models.CharField(max_length=100, null=True)
	lenguaje3 = models.CharField(max_length=100, null=True)
	lenguaje4 = models.CharField(max_length=100, null=True)
	lenguaje5 = models.CharField(max_length=100, null=True)

	class Meta:
		verbose_name='materia'
		verbose_name_plural='materias'

	def __str__(self):
		return '{}'.format(self.Nombre)