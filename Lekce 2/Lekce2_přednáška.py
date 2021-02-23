""" Slovníky a cykly"""

sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

for key in sales.items():
    (
        " tento cyklus projde všechny klíče a klíč uloží do proměné key, musí být sales.items() - tak že pracovat jak s klíčí, \n"
        "tak hodnotamy. Stejně by šlo sales.keys nebo sales.values (pracovala by jen s jednou z dvojice)")

    print(sales)
    """print(sales[key]) - takto by udělal javadeveloper"""
total = 0
for key, value in sales.items():
    """" toto by mělo do key uložit klíče a do value hodnotu klíče, ale musí dát sales.items"""
    print(f"Knihy {key} se prodalo {value} kusů.")
    total +=value
print(f"Celkem bylo prodáno {total} knih")
""" f na začátku - f string)"""

