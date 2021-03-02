"""Kniha
to dáš

Zkus pro našeho nakladatele vytvořit software s využitím tříd a objektů. Vytvoř tedy třídu Book,
která reprezentuje knihu. Každá kniha bude mít atributy title, pages a price. Hodnoty nastav ve funkci __init__.

    Přidej knize funkci getInfo, která vypíše informace o knize v nějakém pěkném formátu.
    Občas se stane, že se kniha moc neprodává a knihkupec se snaží nalákat kupující slevou.
    Přidej funkci discount, která bude mít jeden parametr - velikost slevy v procentech.
    Funkce sníží cenu knihy o dané procento."""

class Book():
     def __init__(self, authors, title, pages, price):
        self.authors = authors
        self.title = title
        self.pages = pages
        self.price = price
     def getInfo(self):
        return f"Kniha {self.title} o {self.pages} stranách za cenu {self.price} Kč"
     def discount (velikost_slevy_procenta):
        self.price = self.price * (1-(discount/100))
        return f"Nyní za cenu {self.price}"
""" lze napsat i zkráceně"""
Hanna = Book("Třeštíková", "Hanna", 250, 350)
Hanna.getInfo()
Hanna.discount(18)
Hanna.getInfo()

"""Příklad 2"""
class Package:
  def deliver(self):
    self.delivered = True
  def getInfo(self):
    if self.delivered:
      deliveredText = "Balík byl doručen"
    else:
      deliveredText = "Balík zatím nebyl doručen."
    print(f"Balík je na adresu {self.address} a váží {self.weightInKilos}. {deliveredText}")
  def __init__(self, address, weightInKilos):
    self.address = address
    self.weightInKilos = weightInKilos
    self.delivered = False

balik = Package("Alfa 6", 20)
balik.getInfo()
balik.deliver()
balik.getInfo()

"""vyzkoušet si a dodělat příklad 3"""