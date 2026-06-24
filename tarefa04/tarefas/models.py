from django.db import models

class Tarefa(models.Model):
    nome = models.CharField(max_length=100)

    STATUS_CHOICES = [
        ('Indeferido', 'Indeferido'),
        ('Em andamento', 'Em andamento'),
        ('Concluída', 'Concluída'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    prazo = models.DateField()

    def __str__(self):
        return self.nome