from django.db import models

# Create your models here.

class Materia(models.Model):
	NombreMateria = models.CharField(max_length=12)
	imagen = models.ImageField(upload_to="materias")
	
	class Meta:
		verbose_name='materia'
		verbose_name_plural='materias'

	def __str__(self):
		return '{}'.format(self.NombreMateria)