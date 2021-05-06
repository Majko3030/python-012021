import pandas
import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")
data = pandas.read_csv('twlo.csv')
#print(data)
print(data.shape)
print(data.iloc[:5])
print(data.head())
print(data.iloc[-1])
pocet_radku = data.shape[0]
zmena= (data.iloc[301, 5]*100/data.iloc[0, 5])
print(f"Hodnota se zvýšila o {zmena} %")
sloupec_high= data.loc[:,"High"]
print(sloupec_high)
print(sloupec_high.max())
sloupec_low= data.loc[:,"Low"]
print(sloupec_low.min())


