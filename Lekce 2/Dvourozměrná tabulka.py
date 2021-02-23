books = [
  {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
  {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
  {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
]
" slovníky dané do seznamu"
total =0
for item in books:
    "u books nemůže být items, není slovník!"
    if item["year"]==2019:

         total += item["sold"] * item["price"]

print(f"Celkové tržby jsou {total}.")

"Úkol 1 - Čtenářský deník"
"""Gustav je vášnivým čtenářem detektive z našeho nakladatelství a navíc si zapisuje knihy, které přečetl. 
Níže ve slovníku vidíme, jaké informace si eviduje - název knihy, počet stran a hodnocení od 0 do 10.

    Napiš program, který spočte celkový počet stran, které Gustav přečetl.
    Připiš do programu výpočet počtu knih, kterým dal Gustav hodnocení alespoň 8.
"""
books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]
total = 0
for item in books:
    total += item["pages"]
print(f"Gustav přečetl {total} stran. ")
pocetKnih = 0
for item in books:
    if item["rating"] >= 8:
        pocetKnih +=1
print(f"Gustav přečet {pocetKnih} knih.")

"""Úkol 2 - Vysvědčení
Uvažujme vysvědčení, které máme zapsané jako slovník.

    Napiš program, který spočte průměrnou známku ze všech předmětů.
    Uprav program, aby vypsal všechny předměty, ve kterých získal student známku 1.

"""
schoolReport = {
  "Český jazyk": 1,
  "Anglický jazyk": 1,
  "Matematika": 1,
  "Přírodopis": 2,
  "Dějepis": 1,
  "Fyzika": 2,
  "Hudební výchova": 4,
  "Výtvarná výchova": 2,
  "Tělešná výchova": 3,
  "Chemie": 4,
}

znamkacelkem = 0
pocetpredmetu = 0
for key, values in schoolReport.items():
    znamkacelkem += values
    pocetpredmetu +=1


prumer = znamkacelkem/pocetpredmetu
""" nebo  sum_marks/len(schoolReport)
je i funkce sum(schoolReport.values()) - to dá sumu za hodnoty (musí být values)"""
print(f"Průměrná známka žáka ze všech předmětů je {prumer}.")

sum_marks = 0
subjects = []
for subject, mark in schoolReport.items():
    sum_marks += mark

    if mark == 1:
        subjects.append(subject)

print(', '.join(subjects))
print(sum_marks / len(schoolReport))
print(sum(schoolReport.values()) / len(schoolReport))

"""Úkol 3
"""
plates = {"4A2 3000": "František Novák",
  "6P5 4747": "Jana Pilná",
  "3B7 3652": "Jaroslav Sečkár",
  "1P5 5269": "Marta Nováková",
  "37E 1252": "Martina Matušková",
  "2A5 2241": "Jan Král"}

for plate, name in plates.items():
    if plate[1]=='P':
        print(name)

""" index  plate[1] - číslo v zárovce index - zde druhý znak(pozice v plate)"""






