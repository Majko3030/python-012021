from django.db import models

# Create your models here.
class Kurz(models.Model):
  nazev = models.CharField(max_length=100)
  zacatek = models.DateTimeField()
  konec = models.DateTimeField()
  popis = models.CharField(max_length=1000)
  cena = models.IntegerField()

  def __str__(self):
      return self.nazev

# název - max_lenght - zadá maximum, aby nedával uživatel mnoho znaků

class Prihlaska(models.Model):
    email = models.CharField(max_length=100)
    jmeno = models.CharField(max_length=100)
    prijmeni = models.CharField(max_length=100)
    motivace = models.TextField()
    kurz = models.ForeignKey(Kurz, on_delete=models.SET_NULL, null=True)