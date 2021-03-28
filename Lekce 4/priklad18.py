"""Inverview

Uvažuj následující třídu Kontakt, která slouží k evidenci všech kontaktů (např. zákazníků, zaměstnanců, uchazečů o práci atd.).

class Kontakt:
  def __init__(self, jmeno, email):
    self.jmeno = jmeno
    self.email = email

Vytvoř třídu Uchazec, která bude dědit od třídy Kontakt a která reprezentuje uchazeče o práci.
Uchazeč o práci bude mít navíc atribut datum_pohovoru a zapis_z_pohovoru.
Datum pohovoru objekt získá z parametru a zápis z pohovoru je na začátku prázdný řetězec "".

Dále přidej funkci uloz_zapis(), která bude mít jako parametr textový zápis pohovoru.
Tato funkce ohlídá, zda uživatel omylem nezadává zápis k pohovoru, který ještě neproběhl.
Na začátku funkce porovnej aktuální datum a datum pohovoru. Pokud podle data pohovor ještě neproběhl, vrať chybový text,
 který informuje uživatele o chybě. Pokud již podle data pohovor proběhl, ulož zápis a vrať text s informací, že zápis byl uložen."""
from datetime import datetime
datum_dnes = datetime.now()

class Kontakt:
  def __init__(self, jmeno, email):
    self.jmeno = jmeno
    self.email = email

class Uchazec(Kontakt):
    def __init__(self, jmeno, email, datum_pohovoru, zapis_z_pohovoru=""):
        super().__init__(jmeno, email)
        self.datum_pohovoru = datum_pohovoru
        self.zapis_z_pohovoru= zapis_z_pohovoru
    def uloz_zapis(self, zapis):
        if datum_dnes > self.datum_pohovoru:
            self.zapis_z_pohovoru = zapis
        else:
            print("Pohovor ještě neproběhl")
    def get_info(self):
        return f"{self.jmeno}, zápis z pohovoru: {self.zapis_z_pohovoru}"

petr = Uchazec("Petr", "pp@seznam.cz", datetime(2021, 3, 29))
zapis = input("Vložte zápis")
print(petr.uloz_zapis(zapis))
print(petr.get_info())