import pandas
staty =pandas.read_json("staty.json")
staty = staty.set_index("name")
print(staty[["population", "area"]])
#dotaz - první tabulka[sloupec]
populace = staty["population"]
#dataframe = tabulka, 1 sloupec z tabulky = serie
#pandas by asi zkousl neunikátní index, ale při práci s daty problém
#print(populace.sum())
#součet, vrátí přímo jako číslo
#print(staty["population"]<1000)
#vypíše všecho, ale True/False - jestli pro daný stát platí či nikoliv

#pidistaty =staty[staty["population"]<1000]
#vypíše státy, kde platí, že vnitřek je True, to už vypíše země s méně než 1000 obyv.
#print(pidistaty[["area","population"]])

print(staty[staty["population"] < 1000])
pidistaty = staty[staty["population"] < 1000]
print(pidistaty[["area", "population"]])
lidnate_evropske_staty = staty[(staty["population"] > 20_000_000) & (staty["region"] == "Europe")]
print(lidnate_evropske_staty["population"])
#kulaté závorky je potřeba pokud více podmínek, podtržítko - program nevším - on si je odebere, proto může být
vyznamne_staty = staty[(staty["population"]>1_000_000_000) |
                       (staty["area"]>3_000_000)]
#alt+w
#závorky mezi | a mezi & musí být, aby pandas zpracoval
print(vyznamne_staty)

#podmínka pro seznam

staty["subregion"].isin(["Western Europe", "Eastern Europe"])
#tímto isin - jako in - vybere jen ty, kde je Wester nebo Easter E.
zap_vych_evropa = staty[staty["subregion"].isin(["Western Europe", "Eastern Europe"])]