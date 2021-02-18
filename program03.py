volnePokoje = {
  9: ["Amadeus", "Goya", "Vlasy"],
  10: ["Forman", "Goya"],
  11: [],
  12: ["Amadeus", "Vlasy"]
}
cas= int(input ("V jaký čas si chceš zamluvit meeting room? "))
zasedacky= volnePokoje[cas]
print(len(zasedacky))

