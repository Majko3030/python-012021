#Balicek
class Package:
    def __init__(self, address, weight):
        self.address = address
        self.weight = weight
        self.delivered = False

    def deliver(self):
        self.delivered = True

    def get_info(self):
        return f'Adresa: {self.address}, Vaha: {self.weight}, Stav doruceni: {self.delivered}'
"""

Pokračuj ve své práci pro zásilkovou společnost. Společnost nově doručuje i cenné balíky, které mají zadanou určitou hodnotu.

    Vytvoř třídu ValuablePackage, která dědí od třídy Package. ValuablePackage má navíc atribut value, ostatní atributy dědí od třídy Package.
    Atribut value nastav pomocí funkce __init__. Ostatní parametry předej funkci __init__ třídy Package.
    Vytvoř si alespoň jeden objekt a zkus volání jeho funkcí.

"""
class ValuablePackage(Package):
    def __init__(self, address, weight, value):
        super().__init__(address, weight)
        self.value = value
    def get_info(self):
        return f"Adresa: {self.address}, Váha: {self.weight}, Stav: {self.delivered}, Hodnota: {self.value}"

Anna_bal= ValuablePackage("Rovného 10, Ol", 10, 200)
print(Anna_bal.get_info())
print(Anna_bal.deliver())