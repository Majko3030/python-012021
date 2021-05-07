import pandas
import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
teplota = pandas.read_csv("temperature.csv")
print(teplota.head())
Praha = teplota[teplota["City"]== "Prague"]
print(Praha)
Nad_80 = teplota[teplota["AvgTemperature"]> 80]
print(Nad_80)
EU_nad_60 = teplota[(teplota["AvgTemperature"]>60)& (teplota["Region"]=="Europe")]
print(EU_nad_60)
Extrem = teplota[(teplota["AvgTemperature"]>80) | (teplota["AvgTemperature"]<-20)]
print(Extrem)