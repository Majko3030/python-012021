from django.db import models

# Create your models here.
class Auto(models.Model):
  registracni_znacka = models.CharField(max_length=100)
  znacka_typ_vozidla = models.CharField(max_length=100)
  pocet_km = models.IntegerField()
  datum_posledni_kontroly = models.DateTimeField()

class Zakaznik(models.Model):
  jmeno = models.CharField(max_length=100)
  prijmeni = models.CharField(max_length=100)
  cislo_ridicského_prukazu = models.CharField(max_length=100)
  datum_narozeni = models.DateTimeField()

class Vypujcka(models.Model):
  datum_zacatku_vypujcky =models.DateTimeField()
  datum_konce_vypujcky =models.DateTimeField()
  cena = models.IntegerField()