from sys import argv

script, filename = argv

print(f"We're goint to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!\n")
target.truncate()

print("Now I'm goint to ask you for three lines.\n")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm goint to write these to the file.\n")
 
target.writelines([line1, "\n", line2, "\n", line3, "\n"])

target = open(filename)
print(f"Let's look at the contents of your file, {filename}:\n")
print(target.read())
print("\n")

confirm = input("Is that your lines? y/n ")
if confirm in ['y', 'Y']:
    print(f"W00t! It works!\n")
else:
    print(f"Crap it didn't work!")
    print(f"Ending this folly now!\n")
    raise SystemExit

print("And finally, we close it.")
target.close()
