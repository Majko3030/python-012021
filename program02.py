sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}
typSoucastky = input("Vložte kód součástky: ")
mnozstvi = int(input("Kolik součástek si chce zákazník koupit? "))

if typSoucastky in sklad:
    if mnozstvi > sklad[typSoucastky]:
        print("lze prodat pouze omezené množství kusů, a to: " + str(sklad[typSoucastky]))
        sklad.pop(typSoucastky)
    else:
        print("poptávku lze uspokojit v plné výši")
        sklad[typSoucastky]=sklad[typSoucastky]-mnozstvi
else:
    print("součástka není skladem")

"print(sklad)"
