#import wget
#wget.download('https://raw.githubusercontent.com/pesikj/progr2-python/master/python-pro-data-1/agregace-a-spojovani/excs/assets/jmena.csv')
#wget.download('https://raw.githubusercontent.com/pesikj/progr2-python/master/python-pro-data-1/agregace-a-spojovani/excs/assets/studenti1.csv')
#wget.download('https://raw.githubusercontent.com/pesikj/progr2-python/master/python-pro-data-1/agregace-a-spojovani/excs/assets/studenti2.csv')
import pandas
studenti1 = pandas.read_csv("studenti1.csv")
studenti2 = pandas.read_csv("studenti2.csv")

#1
student = pandas.concat([studenti1,studenti2], ignore_index = True)
#2
print(student.head())
chyba1 = student[student["ročník"].isnull()]
chyba2 = student[student["kruh"].isnull()]
#print(f"Chybí ročník, nestuduje: {len(chyba1)}")
#nebo přes
print(chyba1.shape)
#print(f"Dalkar: {len(chyba2)}")

#3
ocisteny_student = student.dropna()
#4
obor = ocisteny_student.groupby("obor").count()
print(obor)

#5
prospech = ocisteny_student.groupby("obor")["prospěch"].mean()
print(prospech)

jmena = pandas.read_csv("jmena.csv").dropna()
propojeni = pandas.merge(jmena, ocisteny_student)

pohlavi = propojeni.groupby("pohlaví").count()
print(pohlavi)

#7
if int(pohlavi["jméno"][0]) > int(pohlavi["jméno"][1]):
    print("muži")
else:
    print("ženy")

