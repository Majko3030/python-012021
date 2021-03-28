# union - tabulky dáme pod sebe
# operace join - vedle sebe dle něčeho
import pandas
#import wget
#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/predsedajici.csv")

#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/studenti.csv")
u202 = pandas.read_csv("u202.csv").dropna()
u203 = pandas.read_csv("u203.csv").dropna()
u302 = pandas.read_csv("u302.csv").dropna()
u202["místnost"] = "u202"
u203["místnost"] = "u203"
u302["místnost"] = "u302"
maturita = pandas.concat([u202,u203, u302], ignore_index = True)

studenti = pandas.read_csv("studenti.csv")
#print(studenti.head())

#teď propojíme tabulku studenty a tabulky se známkami z maturit
#vysledky_se_jmeny = pandas.merge(maturita, studenti)
#print(vysledky_se_jmeny.head())
#print(maturita.shape)
#print(vysledky_se_jmeny.shape)
#shape ukáže rozměr tabulky, po snížení o 2 řádky méně
#pandas se dodívá na stejně pojmenované sloupce a spojí dle toho
#inner join - atribut zastoupen v obou
#lefjoin - z 1. tabulky vše, z 2. tabulky, co naplní, jinak prázná hodnota
#righjoin - z 2. tebulky hlavní a z 1. doplní
#outerjoin - splní oboje tabulky - zachová vše z obou

vysledky_se_jmeny = pandas.merge(u202, studenti, how = "left")
print(vysledky_se_jmeny[vysledky_se_jmeny["jmeno"].isnull()])
#ukazuje, jaké hodnoty z tabulky je null u jmena, chybí v seznamu studentů
print(u202.shape)
print(vysledky_se_jmeny.shape)

predsedajici = pandas.read_csv("predsedajici.csv")
predsedajici["den"] = predsedajici["den"].str.strip()
vysledky_se_jmeny_a_predsedajicimi = pandas.merge(vysledky_se_jmeny, predsedajici, on="den")
#když nedefinuje dle čeho, tak vybralo jméno, i když jméno jiný obsah, musí dát on
print(vysledky_se_jmeny.columns)
print(vysledky_se_jmeny_a_predsedajicimi.columns)
print(vysledky_se_jmeny_a_predsedajicimi.head())

# u přednášejících v CSV mezera za pondělí, takže udělá stejně rozdíl jako výše u student
# bude chybět záznamy s chybějícím človíčkem - použít funkci strip - vezme mezery
