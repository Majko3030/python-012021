import pandas
nakupy = pandas.read_csv('nakupy.csv')
#print(nakupy.iloc[:3])
#od 8. nákupu do konce
#print(nakupy.iloc[8:0])
#poslední 3 - s minusem
#print(nakupy.iloc[-3:])
pozdrav = " Ahoj  Andreo "
print(pozdrav[-6])
#jako v iloc lze získat rozsah
print(pozdrav[-6:-3])
print(pozdrav.strip())
#odtraní mezery na začátku a na konci
print(pozdrav.strip().replace("  ", " "))
#print(nakupy.head())
# head první 5, kdy přidá do závorky n=počet výpisů)
#print(nakupy.tail(n=2)
#toto vrátí poslední 5 nebo n= počet řádků vrácených
#print(nakupy.iloc[:5, [0,3]])
#první část řádky, druhá sloupce, pokud jednotlivé tak přes seznam (hranaté závorky)
#print(nakupy.iloc[:, [0,3]])
# toto v případě samotné: - tak vše (když chci vše, ale jen některé sloupce)


