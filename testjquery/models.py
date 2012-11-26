from django.db import models

# Create your models here.
# 
class Usuario(models.Model):
	nombre = models.CharField(max_length=150)
	apellido = models.CharField(max_length=150)
	edad = models.IntegerField()
	twitter = models.CharField(max_length=50)

	class Meta:
		verbose_name = ('Usuario')
		verbose_name_plural = ('Usuarios')

	def __unicode__(self):
		return self.nombre
    
