# Ask for name
print("What is your name human?")
name = str(input(">"))

# Ask for age
print("\nHow old are you (in years)?")
age = int(input(">"))

# Ask for height
print("\nHow tall are you (in meters)?")
height = float(input(">"))

# Ask for weight
print("\nhow much do you weigh (in kilograms?")
weight = float(input(">"))

bmi = weight/(height**2)
limitedbmi = "{:.2f}".format(bmi)

# Calculate BMI and print
print(f"\n{name} you are {age} and your BMI is {bmi}")
