from django.db import models


class Tecnologias(models.Model):
    tecnologia = models.CharField(max_length=30)

    def __str__(self):
        return self.tecnologia

class Empresa (models.Model):

    nicho_mercado = (
       ('M', 'Marketing'),
       ('N', 'Nutrição'),
       ('D', 'Designer'),
       ('T', 'Tecnologia'),
    )

    logo = models.ImageField(upload_to="logo-empresa", null=True)
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    cidade = models.CharField(max_length=30)
    tecnologias = models.ManyToManyField(Tecnologias)
    endereco = models.CharField(max_length=30)
    caractristica = models.TextField()
    nicho = models.CharField(max_length=3, choices=nicho_mercado)

    def __str__(self):
        return self.nome

    def qtd_vagas(self):
        return Vagas.objects.filter(empresa__id=self.id).count()

class Vagas(models.Model):
    choices_experiencia = (
        ('J', 'Júnior'),
        ('P', 'Pleno'),
        ('S', 'Sênior')
    )

    choices_status = (
        ('I', 'Interesse'),
        ('C', 'Currículo enviado'),
        ('E', 'Entrevista'),
        ('D', 'Desafio técnico'),
        ('F', 'Finalizado')
    )

    empresa = models.ForeignKey(Empresa, null=True, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=30)
    nivel_experiencia = models.CharField(max_length=2, choices=choices_experiencia)
    data_final = models.DateField()
    email = models.EmailField(null=True)
    status = models.CharField(max_length=30, choices=choices_status)
    tecnologias_dominadas = models.ManyToManyField(Tecnologias)
    tecnologias_estudar = models.ManyToManyField(Tecnologias, related_name='estudar')

    def progresso(self):
        x = [((i+1)*20,j[0]) for i, j in enumerate(self.choices_status)]
        x = list(filter(lambda x: x[1] == self.status, x))[0][0]
        return x

    def __str__(self):
        return self.titulo
