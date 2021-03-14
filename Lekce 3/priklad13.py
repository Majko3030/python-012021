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
        self.stav_tachometru
        self.dny
    def get_info(self):
        return f"Auto s poznávačkou {self.registr_znacka}, značka {self.znacka} a ujetými {self.km} km, obsazenost je {self.obsazenost}"
    def pujc_auto(self):
        if self.obsazenost:
            self.obsazenost = False
            return print("Potvrzuji zapůjčení vozidla")
        else:
            print("Vozidlo není k dispozici.")
    def vrat_auto(self, stav_tachometru, dny):

auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", "47534")
auto2 = Auto("1P3 4747", "Škoda Octavia", "41253")

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