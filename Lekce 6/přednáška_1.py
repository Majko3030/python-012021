#Agregace a spojování dat
#import wget
#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/u202.csv")
#kdyby chtěli víc na ráz, tak udělat seznam odkazů a pak for soubor (seznam) in soubory: wget.download(seznam)
#import wget
"""soubory = ["https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/u203.csv",
           "https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/u302.csv"]
for soubor in soubory:
  wget.download(soubor)"""
import pandas
#u202 = pandas.read_csv("u202.csv")
#print(u202.head())
"""v datových analíze řeší často odstranění hodnot -neuplné údaje, chybné hodnoty, chybí hodnoty
není dobré hned mazat data"""

#print(u202[u202["znamka"].isnull()])
# říká, na kterých řádcích není vyplněno (uvnitř hranaté závěrky)
# dáním u202[] dá dotaz, který přímo vyfiltruje
u202 = pandas.read_csv("u202.csv").dropna()
#dropna() odmaže hodnoty, kde není vyplněno (řádky)
u203 = pandas.read_csv("u203.csv").dropna()
u302 = pandas.read_csv("u302.csv").dropna()
#ted si spojím tabulky pandas.concat(), dovnitř vložit jako seznam
#maturita = pandas.concat([u202,u203, u302], ignore_index = True)
#print(maturita.loc[1]) - když dám toto, tak 3 řádky, protože spojením mají indexi některé řádky stejné
# toto platí před přidáním ignore_index = True (ignoruje indexy, které jsou někde schodné
#takto se ztratí informace o místnosti, kde maturoval (202,203,302

u202["místnost"] = "u202"
u203["místnost"] = "u203"
u302["místnost"] = "u302"
#tímto vložíme sloupec, který obsahuje informaci o místnosti (souboru), z něhož je řádek
maturita = pandas.concat([u202,u203, u302], ignore_index = True)
print(maturita.head())
#často budeme chtít exportovat data
maturita.to_csv("maturita.csv", index = False)
#index = False - neukládá číslo řádku
#přes pravé kliknutí nad repozitářem - open in -explorer - ukáže na disku
# lze uložit i do excelu maturita.to_excel("maturita.xlsx", index = False)
# k tomu musí nainstalovat modul pro excel
#když bude čas, podívat se, jak zbavit paznaků, když uložíme do CSV
#data > import (pro export do excelu)
