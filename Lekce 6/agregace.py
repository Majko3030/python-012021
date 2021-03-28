# union - tabulky dáme pod sebe
# operace join - vedle sebe dle něčeho
import pandas
#import wget
#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/predsedajici.csv")

#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/studenti.csv")
u202 = pandas.read_csv("u202.csv").dropna()
u203 = pandas.read_csv("u203.csv").dropna()
u302 = pandas.read_csv("u302.csv").dropna()
u202["místnost"] = "u202"
u203["místnost"] = "u203"
u302["místnost"] = "u302"
maturita = pandas.concat([u202,u203, u302], ignore_index = True)

#Agregace
#print(maturita.groupby("místnost").count())
#vypíše, pro jakou místnost bylo kolik předmětů - počet záznamů
#print(maturita.groupby("predmet")["znamka"].mean())
#vypíše průměr dle předmětů, přidáním závorky ["znamka"] zobrazíme průměr jen v daném sloupci
print(maturita.groupby("predmet")["znamka"].max())
print(maturita.groupby("predmet")["znamka"].sum())
#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/progr2-python/03d3b81430e651e03743b19084e935d87dd40ccd/python-pro-data-1/nacteni-dat/assets/nakupy.csv")
nakupy = pandas.read_csv("nakupy.csv")
print(nakupy.groupby("Jméno").sum())