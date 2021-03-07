"Napište funkci mult, která bude mít dva číselné parametry. Funkce oba parametry vynásobí a vrátí výsledek."
def mult(a,b):
    return print(a*b)
mult(3,5)

""""

Napiš funkci totalPrice, která vypočte cenu noci v hotelu. Funkce bude mít dva parametry - persons a breakfast. 
Cena za noc za osobu je 850 Kč a cena za snídani za osobu je 125 Kč. Funkce vrátí výslednou cenu. 
Parametr breakfast je nepovinný a výchozí hodnota je False.

Funkci vyzkoušej se zadáním dvou i jedné hodnoty, např. totalPrice(3), totalPrice(2, True).
"""
def totalPrice(persons, breakfast=False):
    price = 850
    price_breakfast = 125
    if breakfast:
        cenapokoje = persons * (price + price_breakfast)
    else:
        cenapokoje = persons * price
    return (print(f"Cena pokoje je {cenapokoje} Kč"))
totalPrice(10, True)
"""Měsíc narození


Napiš funkce monthOfBirth, která bude mít jeden parametr - rodné číslo. 
Funkce ze zadaného rodného čísla určí měsíc narození, které vrátí jako výstup. 
Nezapomeň, že pro ženy je k měsíci připočtena hodnota 50.

    Příklad: Pro hodnotu 9207054439 vrátí 7. Pro hodnotu 9555125899 vrátí 5.

"""
def monthOfBirth (rodne):
    mesic = rodne[2] + rodne[3]
    if int(mesic)>50:
        mesic= int(mesic) -50
    return print(mesic)
monthOfBirth('9257054439')
#jako rodne [2] + rodne [3] je stejné jako rodne [2:4] - neostrá nerovnost, proto dává až 4

#RULETA

"""

Napiš funkci, která bude jednoduchou simulací rulety. Budeme uvažovat pouze možnost sázení na řady. 
Uživatel si může vybrat jednu ze tří řad:

    první řada (hodnoty 1, 4, 7 atd.),

    druhá řada (hodnoty 2, 5, 8 atd.),

    třetí řada (hodnoty 3, 6, 9 atd.).

    Zeptej se uživatele, na kterou ze tří řad sází a na výši sázky.

    Vytvoř funkci roulette, která bude mít parametry číslo řady a výši sázky. 
    Pomocí funkce randint z modulu random vygeneruj náhodné číslo v rozsahu od 0 (včetně) do 36. V
    yhodnoť, do které řady číslo náleží. Nezapomeň, že 0 nepatří do žádné z řad a pokud padne, 
    uživatel vždy prohrává.

    Funkce roulette vrací hodnotu výhry. Pokud uživatel vsadil na správnou řadu, vyhrává dvojnásobek sázky, 
    v opačném případě nevyhrává nic jeho sázka propadá.

"""
import random
def roulette(rada, sazka):
    n = random.randint(0,36)
    print(f" Hozené číslo je {n}")
    if n == 0:
        return -sazka
    if n%3 == 1 and rada ==1:
        return sazka *2
    if n%3 == 2 and rada ==2:
        return sazka *2
    if n % 3 == 0 and rada == 3:
        return sazka *2
    return - sazka
print(roulette(2,50))