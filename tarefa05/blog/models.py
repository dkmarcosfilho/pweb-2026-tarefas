from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    imagem = models.ImageField(upload_to='posts/')
    data_publicacao = models.DateField(auto_now= True)

    def __str__(self):
        return self.titulo