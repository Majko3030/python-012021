"""
nonverified=['Anna','Hanna','Petr']
verified=[]

while nonverified:
    user=nonverified.pop()
    print(f"User {user} was verified.")
    verified.append(user)
print("These users were verified:")
for veri in verified:
    print(veri)

#7-8 crash course
sandwich_orders=["cheese","pastrami","peperoni","pastrami","mayo","9-80", "pastrami"]
finished_sandwiches=[]

print("Deli run out of pastrami sandwiches.")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    for sandwich in sandwich_orders:
        sand=sandwich_orders.pop()
        print(f"I made you a {sand} sandwich.")
        finished_sandwiches.append(sand)



print("I made these sandwitches for you:")
for sandwich in finished_sandwiches:
    print(sandwich)

wish={}
state=True

while state:
    name=input("What is your name?")
    place= input("What is your wish?")
    wish[name]=place
    repeat=input("Other person wants to join? yes/no")
    if repeat=="no":
        state=False

#for name, response in wish.items():
 #   print(f"{name.title()} wasnts to {response.lower()}.")
"""
def car_descriptions(manufacturer, model_name, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model_name'] = model_name
    return car_info


