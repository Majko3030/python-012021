"""Pokračuj ve své práci pro autopůjčovnu z příkladu 11 a příkladu 12.

Přidej třídě Auto funkci vrat_auto(), která bude mít (krom obligátního self) 2 parametry, a to je stav tachometru při
vrácení a počet dní, po které zákazník auto používal. Ulož stav tachometru do atributu objektu. Nastav vozidlo jako volné.

Dále ve funkci vypočti cenu za půjčení. Cena je 400 Kč na den, pokud měl zákazník celkem auto méně než týden, a 300 Kč
na den, pokud měl zákazník auto déle. Cena je stejná pro obě auta. Vlož cenu do nějakého informativního textu a
ten vrať pomocí klíčového slova return.

Na konec programu (mimo třídu) přidej dotaz na uživatele, kolik kilometrů zákazník ujel a jak dlouo ho měl půjčené.
Poté vypiš informaci o ceně."""


class Auto:
    def __init__(self, registr_znacka, znacka, km,stav_tachometru, dny, obsazenost = True):
        self.registr_znacka = registr_znacka
        self.znacka = znacka
        self.km = km
        self.obsazenost = obsazenost
        self.stav_tachometru= stav_tachometru
        self.dny= dny
    def get_info(self):
        return f"Auto s poznávačkou {self.registr_znacka}, značka {self.znacka} a ujetými {self.km} km, obsazenost je {self.obsazenost}, "
    def pujc_auto(self):
        if self.obsazenost:
            self.obsazenost = False
            print("Potvrzuji zapůjčení vozidla")
        else:
            print("Vozidlo není k dispozici.")
    def cena(self, dny):
        if dny<7:
            cena = 400 * dny
        else:
            cena = 300 * dny
        return f"Cena za půjčení vozu je {cena} Kč."
    def vrat_auto(self, stav_tachometru, dny):
        self.stav_tachometru=stav_tachometru
        self.obsazenost

auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", "47534",200, 0 )
auto2 = Auto("1P3 4747", "Škoda Octavia", "41253", 200, 0)

autopujc = input("Jakou značku si přejete půjčit")

if autopujc== "Peugeot":
    print(auto1.get_info())
    auto1.pujc_auto()
elif autopujc== "Škoda":
    print(auto2.get_info())
    auto2.pujc_auto()
else:
    print("Chybná značka")


autopujc = input("Jakou značku si přejete půjčit")


if autopujc== "Peugeot":
    print(auto1.get_info())
    auto1.pujc_auto()
elif autopujc== "Škoda":
    print(auto2.get_info())
    auto2.pujc_auto()
else:
    print("Chybná značka")

vracene_auto = input("Jaké auto vracíte?")
zakaznik1_dny = int(input("Počet dnů půjčení auta: "))
zakaznik1_km = int(input("Počet ujetých km"))

if vracene_auto== "Peugeot":
    auto1.vrat_auto(stav_tachometru=+zakaznik1_km, dny=zakaznik1_dny)
    print(auto1.cena(dny=zakaznik1_dny))
elif vracene_auto == "Škoda":
    auto2.vrat_auto(stav_tachometru=+zakaznik1_km, dny=zakaznik1_dny)
    print(auto2.cena(dny=zakaznik1_dny))
else:
    print("Chybný typ vozidla")





