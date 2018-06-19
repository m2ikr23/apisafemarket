from django.db import models
from datetime import date

class Usuario(models.Model):
    GENERO = (
        ('F','Femenino'),
        ('M','Masculino'),
        )
        
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=12)
    avatar = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/user.png',blank="True")
    reputacion = models.PositiveIntegerField(null=True)
    seguidores = models.ManyToManyField('self',symmetrical=False,blank=True)


    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fechadenacimiento = models.DateField(verbose_name="cumpleaños",default=date.today)
    direccion = models.CharField(max_length=100,blank=True)
    telefono = models.CharField(max_length=16,blank=True)
    sexo = models.CharField(max_length=2, choices=GENERO,blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.email

    @property
    def obtenerNombre(self):
         return '%s %s' %(self.nombre,self.apellido)
