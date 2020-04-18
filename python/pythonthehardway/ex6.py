# set the values for variables
types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# display the contents of variables you've set above
print(x)
print(y)

# display the values of variables inserted into another string
print(f"I said: {x}")
print(f"I also said: '{y}'")

# set another variable to binary and display the output
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

# set more variables
w = "This is the left side of..."
e = "a string with a right side."

# print the concatinated variables
print(w + e)


