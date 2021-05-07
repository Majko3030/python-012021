import pandas
import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/country_vaccinations.csv")
vakcinace= pandas.read_csv("country_vaccinations.csv")
vakcinace_03=vakcinace[vakcinace["date"] == "2021-03-10"]
print(vakcinace_03[["date", "country", "total_vaccinations"]])
vakcinace_03_1m =vakcinace[(vakcinace["date"] == "2021-03-10") & (vakcinace["total_vaccinations"] > 1000000)]
print(vakcinace_03_1m)
vakcinace_extr =vakcinace[(vakcinace["daily_vaccinations"] < 100000) & (vakcinace["daily_vaccinations"] > 100000)]
print(vakcinace_extr)
