from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
   class GenderChoices(models.TextChoices):
      M = u'M', 'Masculino'
      F = u'F', 'Femenino'
      O = u'O', 'Otro'

   class TypeIdChoices(models.TextChoices):
      CC = u'CC', 'Cédula de ciudadanía'
      TI = u'TI', 'Tarjeta de identidad'
      CE = u'CE', 'Cédula de extranjería'      
      PS = u'PS', 'Pasaporte'

   user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )
   id_number = models.PositiveBigIntegerField( unique=True )
   name = models.CharField( max_length=100 )
   lastName = models.CharField( max_length=100 )
   typeId = models.CharField(max_length=2, choices=TypeIdChoices)
   birthday = models.DateField()
   gender = models.CharField(max_length=1, choices=GenderChoices)
   country = models.CharField(max_length=100)
   region = models.CharField(max_length=200, null=True, blank=True)
   city = models.CharField(max_length=200)
   address = models.CharField(max_length=500)
   phone = models.PositiveBigIntegerField(null=True, blank=True)

   class Meta:
      verbose_name = 'Perfil'
      verbose_name_plural = 'Perfiles'

class Sport(models.Model):
   name = models.CharField( max_length=250 )

class SportHistoryInfo(models.Model):
   user = models.OneToOneField( User, on_delete=models.CASCADE, related_name="usuario_history" )
   intercolegiados = models.BooleanField(default=False)
   inter_fase = models.CharField(max_length=200, blank=True, null=True)
   associated = models.BooleanField(default=False)
   assoc_fase = models.CharField(max_length=200, blank=True, null=True)
   merito_file = models.FileField(upload_to='files', blank=True, null=True)
   anamnesis_file = models.FileField(upload_to='files')
   ci_file = models.FileField(upload_to='files')

class PhysicalInfo(models.Model):
   user = models.OneToOneField( User, on_delete=models.CASCADE, related_name="physical_info" )
   size = models.FloatField()
   weight = models.FloatField()
   imc = models.FloatField()
   masa_muscular = models.FloatField()
   masa_grasa =  models.FloatField()
   grasa_visceral = models.FloatField()
   edad_metabolica = models.SmallIntegerField()
   masa_osea = models.FloatField()
   leger_file = models.FileField(upload_to='files')

class SportHistory(models.Model):
   user = models.ForeignKey( User, on_delete=models.CASCADE, related_name="usuario", null=True )
   sport = models.ForeignKey( Sport, on_delete=models.CASCADE, related_name="sport" )
   years = models.SmallIntegerField()