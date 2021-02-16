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
