"Slovníky"
item = {"title": "Čajová konvička s hrnky", "price": 899, "inStock": True}
title = item["title"]
print(title)
"nebo"
print(item["title"])

print("Vybraný předmět je " +  item["title"] + "a cena je "+ str(item["price"]) + ".")
"lze dát i čárky - rozdíl - když +, tak jeden řetězec, když , tak samostatné řetězce, co jdou po sobě"
"formátovaný režezec - nejdřív dá f a pak úvozovky"
print(f"Vybraný předmět je {item['title']} .")
key = "price"
"lze editovat již existující hodnotu, lze uložit i jako proměnnou"
item[key]=999
"přídání informace do slovníku"
item["weight"]= 0.6
if "weight" in item:
    print(f"Hmotnost předmětu je {item['weight']} ")
else:
    print("hmotnost neexistuje")

item["weight"]= 5
if "weight" in item:
    print(f"Hmotnost předmětu je {item['weight']} ")
else:
    print("hmotnost neexistuje")

"příklad ze stránky, zaměstnanci grilují buřty, potřebují evidenci počtu buřtů"
sausages = {"Jirka": 2, "Naty": 1, "Adam": 4, "Lucka": 2, "Pavča": 2}
print(len(sausages))

"potřebuje odstranit počet buřtů - změní hodnotu přiřazenou klíči Jirka"
sausages["Jirka"]=0
"odstranit úplně hodnotu - odstraní klíč"
sausages.pop("Jirka")

print(len(sausages))

"Úkol 1 - vysvědčení"
vysvedceni = {"čestina" : 2, "matika" : 1, "dějepis": 5}

print(f"Výsledek z předmětu je {vysvedceni['matika']} ")
print(vysvedceni)

"Úkol 2 - detektivky"
sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

sales["Noc, která mě zabila"]= 0
sales["Vrah zavolá v deset"]= sales["Vrah zavolá v deset"] +100
print(sales)
"lze také zadat sales záv. Vrah zavolá v deset záv. +=100"

"Úkol 3 - tombola"
tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}
cislolistku= int(input("zadej číslo svého lístku"))
if cislolistku in tombola:
    "dodělat podmínku, aby našlo v tombole, vytisklo to a zároveń odebralo ze seznamu"
    tombola.pop("cislolistku")
    print(f"Výhra je {tombola['cislolistku']}")
else:
    print("Nevýherní")

    "Úkol 4 - paranoidní večírek"

    passwords = {"Jiří": "tajne-heslo", "Natálie": "jeste-tajnejsi-heslo", "Klára": "nejtajnejsi-heslo"}
    " Pořadatel našeho večírku se stává stále více paranoidním a nyní rozhodl, že každý z hostů bude mít speciální heslo, které je platné jen pro něj. Seznam hostů a jejich hesel je níže. Napiš program, který nejprve zkontroluje, zda je host na seznamu, a pokud tam je, zeptá se ho na heslo a zkontroluje jeho správnost. Hostu na seznamu, který zadá správné heslo, vypíše program text: “Smíš vstoupit.”"
host= input("jméno hosta")
if host in passwords:
    heslo=input("řekni své heslo")
    if passwords["host"]==heslo:
        print("Smíš vstoupit")

else: print("zákaz")
