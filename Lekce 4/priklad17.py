"""Streamovací služba podruhé

Pokračuj ve své práci pro streamovací službu. Služba nyní eviduje uživatele, kteří službu využívají.
Vytvoř třídu Uzivatel, která bude mít atributy uzivatelske_jmeno a delka_sledovani, který udává celkovou délku pořadů,
které uživatel zhlédl. Uživatelské jméno získej jako parametr a délka sledování je na začátku 0.

Třídám Serial a Film přidej funkce get_celkova_delka(), která vrátí celkovou délku filmu/seriálu
(u seriálu je to počet episod násobený délkou jedné episody).

Třídě Uzivatel přidej funkci pripocti_zhlednuti(), která bude mít jeden parametr.
Funkce zvýší atribut udávající celkovou délku sledávní o zadaný parametr.

Vytvoř objekt, který reprezentuje nějakého uživatele. Následně zkus uvažovat situaci, že uživatel zhlédne film a seriál,
 které jsi vytvořil(a) jako objekty. Uživateli připočti délky děl k délce sledování,
 využij k tomu funkci get_celkova_delka() u objektu a seriálu, abys zjistil(a), kolik minut (nebo hodin) videa celkem uživatel zhlédl.

TOTO DÁLE JEŠTĚ NEUDĚLALA!

Nejjednodušší řešení je, pokud si u filmu/seriálu uložíš celkovou délku do pomocné proměnné a tuto pomocnou proměnnou
potom předáš jako parametr funkci pripocti_zhlednuti().
Složitější varianta

V pokročilejší variantě neeviduj pouze délku sledování ale i to, jaké pořady uživatel sledoval.
Namísto délky sledování vytvoř atribut, který bude udávat zhlédnuté pořady (ideální pro tento účel je seznam).
Dále přidej funkci zhledni_polozku(), která do seznamu zhlédnutých pořadů přidá novou položku.

Dále vytvoř funkci delka_sledování() pro uživatele, která projde položky v seznamu a vrátí celkovou délku všech pořadů,
které uživatel zhlédl.

Vytvoř si ukázkové objekty a ověř, že vše funguje."""
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
    def get_celkova_delka(self):
        return self.delka

class Serial(Polozka):
    def __init__(self, nazev, zanr, pocet_epizod, delka_ep):
        super().__init__(nazev, zanr)
        self.pocet_epizod = pocet_epizod
        self.delka_ep = delka_ep
    def get_info(self):
        return f"{super().get_info()}, pocet epizod je {self.pocet_epizod} o délce {self.delka_ep} minut."
    def get_celkova_delka(self):
        return self.pocet_epizod*self.delka_ep
class Uzivatel():
    def __init__(self, uzivatelske_jmeno, delka_sledovani=0):
        self.uzivatelske_jmeno = uzivatelske_jmeno
        self.delka_sledovani = delka_sledovani
    def pripocti_zhlednuti(self, sledovani):
        self.delka_sledovani += sledovani
    def get_info(self):
        print(f"Uživatel {self.uzivatelske_jmeno} shlédl obsah v délce {self.delka_sledovani} minut.")
    def zhledni_polozku(self,zhlednuta_polozka=[]):
        zhlednuta_polozka += self.zhlednuta_polozka


film=Film("Secretly greatly","triller", 100)
serial= Serial("Vincenzo", "drama",20, 50)
#print(serial.get_celkova_delka())
anna = Uzivatel("A87")
#varianta lehčí
#anna.pripocti_zhlednuti(film.get_celkova_delka())
#anna.get_info()



