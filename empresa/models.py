from django.db import models

CHOICES_NICHO=(
    ('M','Marketing'),
    ('N','Nutrição'),
    ('D','Design'),
    ('T','Tecnologia'),
    ('P','Psicologia')
)
class Tecnologia(models.Model):
    tecnologia=models.CharField(max_length=30,null=False,blank=False)
    
    def __str__(self):
        return self.tecnologia

class Empresa(models.Model):
    logo=models.ImageField(upload_to="logo_empresa",null=True,blank=False)
    nome=models.CharField(max_length=100,null=False,blank=False)
    email=models.EmailField(null=False,blank=False)
    tecnologias=models.ManyToManyField(Tecnologia)
    cidade=models.CharField(max_length=100,null=False,blank=False)
    endereco=models.CharField(max_length=100,null=False,blank=False)
    caractetistica=models.TextField()
    nicho=models.CharField(max_length=3,choices=CHOICES_NICHO,null=False,blank=False)
    
    def __str__(self):
        return self.nome
    
    
