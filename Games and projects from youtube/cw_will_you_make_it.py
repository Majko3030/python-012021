# function should return 0 if distance_to_pump if distance to pump < mpg* fuel_left
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return 1 if distance_to_pump <= mpg*fuel_left else 0

print(zero_fuel(50, 25, 2))
print(zero_fuel(100, 50, 1))