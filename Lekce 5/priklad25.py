import pandas
import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
teplota = pandas.read_csv("temperature.csv")
print(teplota.head())
"""
    Dotaz na řádky z 13. listopadu 2017 (sloupec Day musí mít hodnotu 13).
    Dotaz na řádky z 13. listopadu 2017 ze Spojených států amerických (sloupec Day musí mít hodnotu 13 a sloupec Country hodnotu US). Výsledek dotazu si ulož do nové tabulky a použij ji jako vstup pro následující dotaz.
    Pro data z předchozího dotazu napiš dotaz na řádky ve městech (sloupec City) Washington a Philadelphia.
"""
listopad_13= teplota[teplota["Day"]==13]
#print(listopad_13)
listopad_13_USA= teplota[(teplota["Day"]==13)& (teplota["Country"]=="US")]
#print(listopad_13_USA)
Wash_Phili= listopad_13_USA[(listopad_13_USA["City"]=="Washington")|(listopad_13_USA["City"]=="Philadelphia")]
print(Wash_Phili)
