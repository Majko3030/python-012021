"""

Stáhni si soubor jmena.csv, který obsahuje tabulku 100 nejpoužívanějších českých křestních jmen seřazených od nejpoužívanějšího k nejméně používanému. Otevři Python konzoli a pomocí Pandasu načti tuto tabulku jako DataFrame. Jako index zvol sloupec s názvem ‘jméno’.

Datový soubor obsahuje následující sloupečky

    jméno - křestní jméno
    četnost - počet obyvatel ČR mající toto jméno
    věk - průměrný věk nositelů jména
    pohlaví - zda je jméno mužské či ženské
    svátek - datum, kdy má dané jméno svátek
    původ - původ jména

Vyřešte následující úkoly.

    Vypište na konzoli informace o jménu Jiří.
    Vypište na konzoli informace pro jména Martin, Zuzana a Josef.
    Vypište na konzoli informace o všech nejčastějších jménech až po Evu.
    Vypište pouze průměrné věky osob mající jména mezi Martinem a Terezou.
    Vypište průměrný věk a původ pro všechna jména od Libora dolů.
    Vypište sloupečky mezi věkem a původem pro všechna jména v tabulce.

"""
#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/progr2-python/master/python-pro-data-1/zakladni-dotazy/excs/ceska-jmena/assets/jmena.csv")

import pandas
jmena =pandas.read_csv('jmena.csv')
jmena = jmena.set_index("jméno")

print(jmena.loc["Jiří"])
print(jmena.loc[["Martin", "Zuzana","Josef"]])

print(jmena.loc[:"Eva"])
print(jmena.loc["Martin":"Tereza","věk"])
print(jmena.loc["Libor":,"věk"])
print(jmena.loc[:,"pohlaví":"svátek"])

"""


