from django.db import models

# Create your models here.
class Kontakt(models.Model):
  jmeno = models.CharField(max_length=50)
  prijmeni = models.CharField(max_length=50)
  email = models.CharField(max_length=100)
  datum_posledniho_kontaktu = models.DateTimeField()

class Organizace(models.Model):
  jmeno = models.CharField(max_length=100)
  ico = models.CharField(max_length =100)
  ulice = models.CharField(max_length=100)
  psc = models.CharField(max_length=100)
  mesto= models.CharField(max_length =100)