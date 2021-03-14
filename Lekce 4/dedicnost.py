class Employee:
  def takeHoliday(self, days):
    if self.remainingHolidayDays >= days:
      self.remainingHolidayDays -= days
      return f"Užij si to."
    else:
      return f"Bohužel už máš nárok jen na {self.remainingHolidayDays} dní."
  def getInfo(self):
    return f"{self.name} pracuje na pozici {self.position}."
  def __init__(self, name, position):
    self.name = name
    self.position = position
    self.remainingHolidayDays = 25

class PartTimeEmployee(Employee):
    def __init__(self, name, position, workload):
        super().__init__(name, position)
        self.workload = workload
    def getInfo(self):
        return f"{super().getInfo()}Je to brigádník, na {self.workload} úvazek"
"přes super().funkce zmateřské, co chci volad" \
"nelze umazat u def __init__ v podtřídě PartTimeEmployee - od je přijímá," \
"ale aby mohl být nastaven - to musí dostat od programátora" \
"bližší funkce třídy než rodiče (nadřazená třída) - pokud není" \
"v třídě, tak až pak jde k rodiči"

import wget
wget.download("http://nove.kodim.cz/czechitas/progr2-python/python-pro-data-1/nacteni-dat/assets/nakupy.csv")

brigadnik = PartTimeEmployee("Jirka Pesik", "brigadnik ve skladu", 0.5)
print(brigadnik.getInfo())