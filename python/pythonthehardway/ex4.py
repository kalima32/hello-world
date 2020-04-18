##Module 4 variables

# comment 1
cars = 100
# comment 2
space_in_a_car = 4.0
# coment 3
drivers = 30
# comment 4
cars_not_driven = cars - drivers
# comment 5
passengers = 90
#comment 6
cars_driven = drivers
# comment 7
carpool_capacity = cars_driven * space_in_a_car
# comment 8
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, 
      "in each car.")

## Traceback (most recent call last)
##    File "ex4.py", line 8, in <module>
##      average_passengers_per_car = car_pool_capacity / passenger
## NameError: name 'car_poo_capacity' is not defined

## This error is simply citing that the variable is not found and doesn't have
## a value


