"""Klíč k úspěchu

Obchodníci v naší softwarové firmě používají jednoduchý systém, aby odhadli šanci na úspěch potenciální zakázky.
Každé zakázce přiřadí body od 0 do 10 a platí:

    Pokud má zakázka méně než 5 bodů, šance na záskání je malá.
    Pokud má zakázka 6 až 8 bodů, šance na získání je střední.
    Pokud má zakázka více bodů, šance na získání je vysoká.

Body přidělují podle následujících kritérií:

    Odvětví: Firma nejlépe prodává do automotive, o něco hůře do retailu.
    Pokud potenciální zákazník podniká v automotive, přičti 3 body, pokud v retailu, přičti 2 bod, jinak 0.
    Obrat: Firma nejlépe prodává zákazníkům se středním obratem. U malých většinou neuspěje, u velkých občas ano.
     Pokud má firma obrat menší než 10 mil. Euro, přičti 0. Pokud je mezi 10 a 1 000 mil. Euro,
     přičti 3 body, jinak 1 bod.
    Země: Firma je nejúspěšnější v Česku a na Slovensku (2 body), o něco méně v Německu a ve Francii (1 bod).
    Ostatním zemím dej 0.
    Konference: Firma loni pořádala odbornou konferenci pro zákazníky. Pokud se zákazník konference účastnil,
    přičti 1 bod, jinak 0.
    Newsletter: Firma též rozesílá newsletter o svém produktu. Pokud zákazník newsletter odebírá, přičti 1 bod.

Napiš funkci, které bude mít 5 parametrů, které reprezentují zadaná kritéria.
Poslední dvě kritéria zadej jako nepovinná s výchozí hodnotou False.
Funkce vrátí šanci na získání zakázky jako řetězec."""

def ocekavany_vysledek(odvetvi,obrat, zeme, konference=False, newsletter=False):
    vysledek = 0
    if odvetvi =="automotive":
        vysledek +=3
        if odvetvi == "retail":
            vysledek +=2
    if 10000000 < obrat < 1000000000:
        vysledek+=3
        if obrat >=100000000:
            vysledek +=1
    if zeme == "Česko" or zeme == "Slovensko":
        vysledek +=2
        if zeme == "Německo" or zeme =="Francie":
            vysledek+=1
    if konference:
        vysledek +=1
    if newsletter:
        vysledek +=1
    if vysledek <5:
        return print("malá šance")
    elif vysledek <9:
            return print("střední šance")
    else: return print("vysoká šance")

ocekavany_vysledek("automotive", 2000000000,"Slovensko", True, False)
ocekavany_vysledek("textil", 200,"Francie")