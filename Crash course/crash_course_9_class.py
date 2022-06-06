class Restaurant:
    def __init__(self, restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(f"Name of the restaurant is : {self.restaurant_name} and they cook {self.cuisine_type}.")
    def open_restaurant(self):
        print("Restaurant is open.")
    def set_number_served(self,guests):
        self.number_served=guests
    def increment_number_served(self,guest):
        self.number_served +=guest

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name, cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavor=["jahodova","malinova","vanilka"]
    def display_flavors(self,flavor):
        print("Máme tyto zmrzliny:")
        for zmrzlina in flavor:
            print(zmrzlina)
icecream=IceCreamStand("Zmrzka","zmrzlina")
print(icecream.display_flavors(["jahoda","malina"]))


restauraceJana = Restaurant("Jana","italská")
restauraceJana.increment_number_served(6)
print(restauraceJana.number_served)
#print(restauraceJana.restaurant_name)
#print(restauraceJana.cuisine_type)
#restauraceJana.describe_restaurant()
#restauraceJana.open_restaurant()
restauraceHana = Restaurant("Hana","svedska")
restauraceKana = Restaurant("Kana","indická")
#restauraceKana.describe_restaurant()
#restauraceHana.describe_restaurant()

class User:
    def __init__(self, first_name, last_name, hobby, sign):
        self.first_name= first_name
        self.last_name= last_name
        self.hobby=hobby
        self.sign=sign
        self.login_attempts=0
    def greet_user(self):
        print(f"Hi {self.first_name } {self.last_name}")
    def describe_user(self):
        print(f"User {self.first_name} {self.last_name}, Hobbys: {self.hobby} and star sign {self.sign}")
    def increment_login_attempts(self):
        self.login_attempts+=1
    def reset_login_attempts(self):
        self.login_attempts=0

class Admin(User):
    def __init__(self,first_name, last_name,hobby, sign,privileges=12):
        super().__init__(first_name,last_name, hobby, sign)
        self.privileges=privileges
    def show_privileges(self, privileges):
        print("List of priviledges:")
        for privilege in privileges:
            print(privilege)

Ana_admin=Admin("Anna","Malá","čtení","škorpion")
"""zjistit, proč nefunuje privileges primární hodnota zadaná v třídě!"""
Hana = User("Hana","Malá", "pletení","štír")
Kana = User("Kana","Velká","čtení", "střelec")
#Hana.greet_user()
#Kana.greet_user()
#Hana.describe_user()
#Kana.describe_user()
Hana.increment_login_attempts()
Hana.increment_login_attempts()
Hana.increment_login_attempts()
print(Hana.login_attempts)
Hana.reset_login_attempts()
print(Hana.login_attempts)