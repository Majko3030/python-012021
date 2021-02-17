baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

cisloBaliku= input("Vložte číslo balíku: ")

if cisloBaliku in baliky:
    if baliky[cisloBaliku] == True:
        print("Balík byl předán kurýrovi")
    else:
        print("Balík zatím nebyl předán kurýrovi")
else:
    print("Chybné číslo balíku")