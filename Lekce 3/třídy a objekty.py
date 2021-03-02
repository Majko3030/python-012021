class Employee:
    def get_info(self):
        return f"{self.name} pracuje na pozici {self.position}"
    def __str__(self):
        return self.name +", " + self.position + ", " + str(self.holidays)
    def __init__(self, name, position, probation=False):
        self.name = name
        self.position = position
        self.holidays = 25
        self.probation = probation

        """init funkce - spouští ve chvíli, když objekt vytvářím
    - na řádku 6 a 10 se spustí init; do závěrky dám objekty
    name a position je něo jiného než self.name a self.position
    zde name - parametr funkce init, nedostane se do get_info funkce
    funkce init udělá, co dělali ručně - zjistit jméno a pozici
    jména různé, jako atribut i něco, co není parametr funkce
    probation nepovinný parametr, přednastaveno False, ale můžu zadat probation)
    atributy vždy self.xxxx"""
"""self - umožnuje, aby objekt pracoval se svými hodnotami; self říkám - že chci pracovat
s konkrétním atributem
konvence - python self, javascript this, vytvoříme nyní objekt"""

"""frantisek = Employee()
vytvořit objekt ze třídy employee - název třídy a prázdné závorky (tam by se 
dávaly atributy, ještě nic nedá, nemá jmené, position)
frantisek.name = "František Novák"
frantisek.position = "konstruktér"
print(frantisek.get_info())
funkce get_info neexistuje bez class Employee
klara = Employee()
klara.name = "Klára Nová"
klara.position = "konstruktérka"
print(klara.get_info())
vypíšou každý zvlášt - objekty na sobě nezávyslé"""

hanna = Employee("František Novák", "konstruktér")
petr = Employee("Petr Malý","fotograf")
print(hanna)
"""po zadání funkce init, tak vloží pol jako při definování výše"""
"funkce str převede objekt na řetězec, a ten už obsahuje hodnotu atributu name!"

""" funkce get_info - musí zavolat (print(frantise.get_info())
pokud funkce není zavolaná, tak nespustí, vyjímka init, str jen přes print)"""

"pokud chci při printu vytisknout, tak musím vypsat viz. return u __str__, případně" \
"by šlo vrátit přes cykli" \
"objekt sám o sobě se nevypíše do řetězce"

print(hanna.__dict__)
"""___dict___ vytvoří slovník, ale přijde se o funkce"""

