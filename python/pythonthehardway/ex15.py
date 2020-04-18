# import argv from sys module for using arguments
from sys import argv

# call 2 variables, and set the second one to a command line argument
script, filename = argv

# 
txt = open(filename)

#print("Here's the value of {txt}\n")

# display output 
# display the output reading the file object.
print(f"Here's your file {filename}:")
print(txt.read())

txt.close()
#print("Type the filename again:")
#file_again = input("> ")

#txt_again = open(file_again)

#print(txt_again.read())
