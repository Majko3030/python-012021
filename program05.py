prodeje2019 = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

prodeje2020 = {
    "Zkus mě chytit": 3157,
    "Vrah zavolá v deset": 3541,
    "Vražda podle knihy": 2510,
    "Past": 2364,
    "Zločinný steh": 5412,
    "Zkus mě chytit": 6671,
}
prodeje2020.pop("Zkus mě chytit")
prodeje2020["Zkus mě chytit"] = (3157+6671)
"""print(prodeje2020)"""
kniha = input("Prodeje které knihy bys chtěl vidět? ")

if kniha in prodeje2019:
    print(prodeje2020[kniha]+prodeje2019[kniha])
elif kniha in prodeje2020:
    print(prodeje2020[kniha])
else:
    print('Chyba v názvu knihy')

"duplicity ve slovníku?"