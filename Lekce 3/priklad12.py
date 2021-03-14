"""Pokračuj ve své práci pro autopůjčovnu, kterou jsi začala v příkladu 11.

Třídě Auto přidej funkci pujc_auto(), která nebude mít (kromě obligátního self) žádný parametr. Funkce zkontroluje,
jestli je vozidlo aktuálně volné. Pokud je volné, vrátí text "Potvrzuji zapůjčení vozidla" a změní hodnotu atributu,
který určuje, zda je vozidlo půjčené. Pokud je vozidlo již půjčené, vrátí text "Vozidlo není k dispozici".

Dále tříde Auto přidej funkci get_info(), která vrátí informaci o vozidle
(stačí registrační značka a značka a typ vozidla) jako řetězec.

Nakonec do programu (mimo třídu) napiš dotaz na uživatele, jakou značku si uživatel přeje půjčit.
Uživatel může zadávat hodnoty Peugeot nebo Škoda. Jakmile si uživatel vybere značku, vypiš informaci o vozidle pomocí
funkce get_info() a následně použij funkci pujc_auto.

Dotaz na uživatele a výpis výsledků si v programu zkopíruj, abys dokázala otestovat, že funkce nedovolí půjčit stejné auto dvakrát."""

class Auto:
    def __init__(self, registr_znacka, znacka, km, obsazenost = True):
        self.registr_znacka = registr_znacka
        self.znacka = znacka
        self.km = km
        self.obsazenost = obsazenost
    def get_info(self):
        return f"Auto s poznávačkou {self.registr_znacka}, značka {self.znacka} a ujetými {self.km} km, obsazenost je {self.obsazenost}"
    def pujc_auto(self):
        if self.obsazenost:
            self.obsazenost = False
            return print("Potvrzuji zapůjčení vozidla")
        else:
            print("Vozidlo není k dispozici.")

auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", "47534")
auto2 = Auto("1P3 4747", "Škoda Octavia", "41253")

print(auto1.get_info())
print(auto1.get_info())

auto_zapujceni = input("Jakou značku si přejete půjčit")

if auto_zapujcení = ( "Peugeot" or "Škoda"):

else:
    print("Chybná značka")