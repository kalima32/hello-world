first_name = "bob"
last_name = "johnson"
whole_name = first_name.title() + " " + last_name.title()
famous_first_name = "groucho"
famous_last_name = "marx"
famous_whole_name = famous_first_name.title() + " " + famous_last_name.title()

print(f"This is practice with names!")
print(first_name.title() + " " + last_name.title())
print(first_name.upper() + " " + last_name.upper())
print(first_name.lower() + " " + last_name.lower())

print(f"Very nice to meet you {whole_name}! Welcome to my python world.")

print(f"\nNow I'll share one of my favorite quotes:\n")
print(f'\t{famous_whole_name} said, "Please accept my resignation.')
print(f"\tI don't want to belong to any club that accepts people.")
print(f'\tpeople like me as members."')
