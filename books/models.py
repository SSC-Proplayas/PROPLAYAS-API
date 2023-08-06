from django.db import models

# Create your models here.

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    pdf = models.FileField(upload_to='libros/')
    cover_image = models.ImageField(upload_to='libros/')

    
    def __str__(self):
        return self.title
