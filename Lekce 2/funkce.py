"""funkce"""
def greetUser():
    print("Ahoj")
""" funkce nadefinovaná jako print, takže když zadám viz. níže, tak vytiskne"""
greetUser()

"""většina funkcí potřebuje nějaký vstup, ten se zadává do (), proměnná definovaná ve funci
funguje pouze v té funkci!!!"""

def greetUser(name):
    print(f"Ahoj {name}")

greetUser("Jirko")
jmeno = input("Napiš jméno")
greetUser(jmeno)

def sumTwoNumbers(a, b):
    return a + b

"""vrátit něco, funkce končí po return """
print(sumTwoNumbers(5,4))

def codeMelater(part1, part2):
    pass
"""pass umožní přeskočit, vytvořit prázdnou funkci"""


def getMark(points, bonus=0):
  if points + bonus <= 60:
    mark = 5
  elif points + bonus <= 70:
    mark = 4
  elif points + bonus <= 80:
    mark = 3
  elif points + bonus <= 90:
    mark = 2
  else:
    mark = 1
  return mark

points = int(input("počet bodů zadej"))
""" musí být číslo, proto int"""
mark = getMark(points)
bonus = int(input("vlož bonus"))
marks = getMark(points, bonus)
print(marks)
""" pokud bonus jako test po zjištění první známky"""
if mark == 5:
    points = input ("Počet bodů z opravného testu")
    points = int(points)
    mark = getMark(points)
print(f"Výsledná známka je {mark}")
