#import wget
#wget.download("http://nove.kodim.cz/czechitas/progr2-python/python-pro-data-1/nacteni-dat/assets/nakupy.csv")

#import wget - jednoduchý, lze stáhnout z internetu přes něj i jiné formáty
import pandas
nakupy = pandas.read_csv('nakupy.csv')
print(nakupy)
nakupy.info()
#to vypíše informace o datech - kolik záznamů, jaké sloupce a kolik hodnot non-null
# a typ položky (int, object,..)
print(nakupy.shape)
#to vrátí hodnotu (11, 4) - 11 řádků a 4 sloupce,
#stejně jako ze seznamu , když dáme nakupy.shape[0] -tak vrátí 1. položku
print(nakupy.columns)
#vypíše, jaké sloupce mám v datech

#Indexy
#funkce iloc - slouží k vybrání 1 konkrétního nákupu
print(nakupy.iloc[3])
#vypíše všechny informace, co tam jsou
# dataframe - technikcý název v pandas tabulka (uložiště, místo, kam můžeme načíst tabulku)
#jeden řádek se uloží do serie přes iloc
print(nakupy.iloc[0:5])
