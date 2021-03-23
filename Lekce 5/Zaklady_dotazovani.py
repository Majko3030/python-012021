#import wget
#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/zakladni-dotazy/assets/staty.json")
import pandas
staty =pandas.read_json("staty.json")
staty = staty.set_index("name")
#když z name (jednoho slouhopce) dá klíč - není standardní sloupec, ale
#chová jako indes (klič) - nenechá se vypsat viz. print(staty.index, ale
#iloc neřeší,jestli sloupec je index či ne - pracuje s číslem řádku
#soubor dle json - načte do stejné struktury, od řádku 5 - neeší
#kde se data vzali - je jedno jaký formát
#print(staty.info())
#print(staty.index)
#toto dá informaci o indexu
#print(staty.loc["Czech Republic"])
#toto vytiskne řádek s indexem v závorce
print(staty.loc["Czech Republic":"Dominican Republic"])
# zde jiné než v iloc - zde i krajní hodnota zobrazí - takže i Dominica zobrazí
#print(staty.loc[:"Dominican Republic"] - lze i takto od začátku po Dom.
#print(staty.loc[["Czech Republic", "Slovakia"], "capital"])
#jako řádky lze omezit i sloupce"
#index bude vždycky při volání tabulky
