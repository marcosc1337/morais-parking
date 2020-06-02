from djongo import models

class Veiculo(models.Model):

   
    placa = models.CharField(max_length=7, null=False, unique=True)
    proprietario = models.CharField(max_length=50, null=False, unique=True)
    matricula = models.BigIntegerField(unique=True)
    curso = models.CharField(max_length=50, null=False)
    area_especial = models.BooleanField() 

    def __str__(self):
        return self.proprietario
        
class Entrada(models.Model):
    SETOR_TYPE_CHOICES = (
        (1, 'setor A Funcionarios'),
        (2, 'setor B Geral'),
        (3, 'setor C Geral'),
        (4, 'setor D Geral'),
    )

    setor_type = models.PositiveSmallIntegerField(choices=SETOR_TYPE_CHOICES)
    placa = models.CharField(max_length=7, null=False, unique=True)
    date_joined = models.DateTimeField('Data de entrada', auto_now_add=True)
