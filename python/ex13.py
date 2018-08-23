from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

fourth = input("We need to capture the 4th argument inline:" )
multi1 = int(input("Give me a number to multiply:" ))
multi2 = int(input("I will need a second number to multiply by:" ))
total = multi1 * multi2
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print("Your fourth variable is:", fourth)
print("This is your total:", total)
