import pandas
import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
teploty = pandas.read_csv("temperature.csv")

"""
    Vyfiltruj si informace o teplotách 13. listopadu 2017.
    Vyřaď všechny záznamy, které mají teplotu -99, protože tato hodnota je pravděpodobně chybná.
    Seřad hodnoty v souboru podle teploty od největší po nejmenší.
    Vypiš pět měst s nejvyšší teplotou a pět měst s nejnižší teplotou.
"""
teploty_13_11 = teploty[teploty["Day"]==13]
print(teploty_13_11)
teploty_13_11_bez_99= teploty_13_11[teploty_13_11["AvgTemperature"] != -99]
print(teploty_13_11_bez_99)
sezareny_vyber_teplot = teploty_13_11_bez_99.sort_values(by="AvgTemperature", ascending = False)
sezareny_vyber_teplot2= sezareny_vyber_teplot[["City","AvgTemperature"]]
print(sezareny_vyber_teplot2.head())
print(sezareny_vyber_teplot2.tail())
