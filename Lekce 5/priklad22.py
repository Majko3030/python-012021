import pandas
import wget
import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/character-deaths.csv")

list_umrti = pandas.read_csv("character-deaths.csv")

list_umrti = list_umrti.set_index("Name")
print(list_umrti.columns)
print(list_umrti.loc["Hali"])
print(list_umrti.loc["Gevin Harlaw": "Gillam"])
print(list_umrti.loc["Gevin Harlaw":"Gillam", ["Death Year"]])
print(list_umrti.loc["Gevin Harlaw":"Gillam", "GoT":"DwD"])