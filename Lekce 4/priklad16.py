#Streamovací služba

"""Uvažuj, že vyvíjíš software pro službu, která nabízí streamování videa. S
lužba nabízí dva typy pořadů - filmy a seriály. Firma chce evidovat, které filmy a seriály nabízí a jejich žánry.
Dále chce u filmů evidovat délku a u seriálů počet episod a délku jedné episody.

    Vytvoř program, který bude obsahovat tři třídy - Polozka, Film a Serial.
    Třída Polozka bude sloužit jako základ pro další třídy. Bude mít atributy určující název a žánr.
    Oba atributy nastav ve funkci __init__(), žánr získej jako parametr funkce.
    Třída Film bude potomkem třídy Polozka. Film má kromě názvu a žánru atribut délka.
    Třída Serial bude potomkem třídy Polozka. Má kromě názvu a žánru atributy počet epizod a délka epizody.
    Všem třídám přidej funkci get_info(), která vypíše informace o položce, resp. o filmu a seriálu.
    Funkce u třídy Polozka vypíše název a žánr. Následně tuto funkci využij ve funkcích u tříd Film a Serial a
    přidej k ní informaci o délce, resp. počtu episod.

Po naprogramování si vytvoř alespoň jeden objekt reprezentující film a seriál o ověr, že vše funguje."""

class Polozka:
    def __init__(self, nazev, zanr):
        self.nazev = nazev
        self.zanr = zanr
    def get_info(self):
        return f"Název je {self.nazev}, žánr je {self.zanr}"

class Film(Polozka):
    def __init__(self, nazev, zanr, delka):
        super().__init__(nazev, zanr)
        self.delka = delka
    def get_info(self):
        return f"{super().get_info()}, delka filmu je {self.delka} minut."

class Serial(Polozka):
    def __init__(self, nazev, zanr, pocet_epizod, delka_ep):
        super().__init__(nazev, zanr)
        self.pocet_epizod = pocet_epizod
        self.delka_ep = delka_ep
    def get_info(self):
        return f"{super().get_info()}, pocet epizod je {self.pocet_epizod} o délce {self.delka_ep} minut."
film=Film("Secretly greatly","triller", 100)
serial= Serial("Vincenzo", "drama",20, 50)

print(film.get_info())
print(serial.get_info())