def display_message():
    print("We learn about functions.")

def make_shirt(size, message=""):
    if message:
        print(f"Vaše tričko bude mít velikost {size} a zprávu: {message}.")
    else:
        print(f"Vaše tričko bude mít velikost {size}.")

#make_shirt("M","YES")
#make_shirt(size="S")

def city_country(city, country):
    print(f"'{city.title()}, {country.title()}'")

#city_country("los angeles", "USA")

def make_album(artist_name,album_title):
    return {'artist':artist_name, 'album':album_title}

#print(make_album('Shakira','Todo'))

while True:
    print("Pokud budete chtít ukončit program, stiskněte s")
    name= input("Jaké je jméno interpreta?")
    if name=="s":
        break
    album= input("Jaké je jméno alba?")
    if album=="s":
        break
    dictionary= make_album(name,album)
    print(dictionary)
    break

list=["yes","no","maybe","another time"]
def show_messages(message):
    for messa in message:
        print(messa)
#show_messages(list)
print(list)

def sent_message(listsx,name=[]):
    while listsx:
         for list in listsx:
             m1=listsx.pop()
             print(m1)
             name.append(m1)
    print(listsx)
    print(name)

#sent_message(list[:])
#print(list)

def making_sandwitch(*toppings):
    print(f"pizza obsahuje:")
    for topping in toppings:
        print(f"-{topping}")

#making_sandwitch("cheese","ham","meat")

def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

user_profile = build_profile("Anna","Bleda",location = "Prague", field = "Economics")
print(user_profile)

def car_description(manufacturer, model_name, **car_info):
    """funkce vrací slovník s informací o vloženém autu"""
    car_info['manufacturer'] = manufacturer
    car_info['model_name'] = model_name
    return car_info

#car = car_description("subaru","outback",color='blue',tow_package=True)
#print(car)
import crash_course_1
print(crash_course_1.car_descriptions("subaru","outback",color='blue',tow_package=True))




