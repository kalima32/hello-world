# defines a simple function to output the amount of cheese and  crackers
# to standard out.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# prints a simple statement then passes, two integers as arguments to 
# my function
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


# prints a simple statement then set's the value for two variables
# then passes those variables to our function
print("OR, we can use variable from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# prints a simple statement, then calculates two variables to pass to
# our function
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# prints a simple statment, then uses our previously defined variables
# to calculate the arguments to pass to our function.
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print("This is my function about cheese and crackers:")
cheese_and_crackers(10 / 5 * amount_of_cheese + 100, amount_of_crackers * 52 /
        12)
