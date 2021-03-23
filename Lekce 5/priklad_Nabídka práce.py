"""

Stáhni si soubor DataAnalyst.csv se seznamem nabídek práce pro datové analytiky. Soubor byl stažen z webu Kaggle.com, kde najdeš spoustu zajímavých dat, na kterých se můžeš učit, jak analyzovat data.

Ale zpět k našim úkolům.

    Načti data do DataFrame, který si pojmenuj jobs.
    Nech si zobrazit názvy sloupců, které jsou v souboru uloženy.
    Podívej se, kolik má soubor řádek.
    Zjisti všechny informace o pracovní pozici na desátém řádku.
    Podívej se, kde budou pracovat zájemci vybraní na dvanáctou až dvacátou pozici.

"""
#import wget
#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/nacteni-dat/excs/nabidky/assets/DataAnalyst.csv")
import pandas
jobs = pandas.read_csv('DataAnalyst.csv')
print(jobs.columns)
print(jobs.info())
print(jobs.iloc[9])
print(jobs.iloc[11:20, 6])
