from django.db import models
from datetime import date
from users.models import Usuario

class Publicacion(models.Model):

    CATEGORIAS= (
        ('Computación','Computación'),
        ('Eléctrodomesticos','Eléctrodomesticos'),
        ('Teléfonos','Teléfonos'),
        ('Accesorios','Accesorios'),
        ('Otros','Otros')
    )

    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)
    descripcion = models.TextField(blank=True,max_length=150)
    precio = models.FloatField()

    def __str__(self):
        return self.descripcion
    
class Foto(models.Model):

    publicacion = models.ForeignKey(Publicacion,on_delete=models.CASCADE)
    foto = models.ImageField(upload_to = 'pic_folder/',blank="True")


class Comentario(models.Model):

    autor= models.ForeignKey(Usuario,on_delete=models.CASCADE)
    comentario = models.TextField(max_length=150,blank=True)
    puntuacion = models.PositiveIntegerField()
    publicacion = models.ForeignKey(Publicacion,on_delete=models.CASCADE)
    
    def __str__(self):
        return '%s %s' %(self.autor, self.comentario)

