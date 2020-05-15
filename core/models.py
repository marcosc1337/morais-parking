from djongo import models

class Veiculo(models.Model):

   
    placa = models.CharField(max_length=7, null=False, unique=True)
    proprietario = models.CharField(max_length=50, null=False, unique=True)
    matricula = models.BigIntegerField(unique=True)
    curso = models.CharField(max_length=50, null=False)
    area_especial = models.BooleanField() 

    def __str__(self):
        return self.proprietario