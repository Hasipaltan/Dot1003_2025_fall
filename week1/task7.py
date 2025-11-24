weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))
print(f"Your BMI is: {weight / (height / 100) ** 2}")