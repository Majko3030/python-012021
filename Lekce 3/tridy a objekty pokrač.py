class Employee:
    def take_holiday(self, days):
        if self.holidays >= days:
             self.holidays = self.holidays - days
            return "Dovolená schválena."
        else:
            return f"Můžeš si vzít pouze {self.holidays} dnů"
    def get_info(self):
        return f"{self.name} pracuje na pozici {self.position}"
    def __str__(self):
        return self.name +", " + self.position + ", " + str(self.holidays)
    def __init__(self, name, position, probation=False):
        self.name = name
        self.position = position
        self.holidays = 25
        self.probation = probation

hanna = Employee("František Novák", "konstruktér")
petr = Employee("Petr Malý","fotograf")

""" lze i -=days"""

print(hana.take_holidays(10))
print(hana.take_holidays(10))

"""nefunguje, proč?"""
