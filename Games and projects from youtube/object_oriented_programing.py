#https://www.youtube.com/watch?v=JeznW_7DlB0
dog="dog"
print(dog.upper())
print(dog.lower())
print(dog.title())
x=1
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.name = Dog("Tim") a to dává hodnotu aributu
        # init spustí automaticky vždy, kdy v kodu bude class Dog (Dog("Tim")
    def add_one(self, x):
        #need to have both argument - self and the x (does not work witouh x in argument)
        return x + 1
    def get_name(self):
        return self.name
    def bark(self):
        print("bark")
    def get_age(self):
        #self musí být vždy - odkaz na isntance (d)
        return self.age
    def set_age(self, age):
        self.age = age
        #changes the age after calling of method (must put argument)
    #method - function in class

d = Dog("Tim",20)
print(d.name)
#call it - instance + name = name(one value)
print(d.get_name())
# d is instance of class Dog, type dog
print(type(d))
#shows class ¨__main.Dog' - object of class dog, main - kde class vytvořena (maind depository
d.bark()
print(d.add_one(5))
#call method on d object
#class upperclass name!
print(d.get_age())
