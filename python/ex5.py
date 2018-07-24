name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
metric_height = 2.54 * height # centimeters
weight = 180 # pounds
metric_weight = 0.4535924 * weight #kilograms
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"His height in centimeters is {metric_height}.")
print(f"He's {weight} pounds heavy.")
print(f"His weight in kilograms is {metric_weight}.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is trick, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

