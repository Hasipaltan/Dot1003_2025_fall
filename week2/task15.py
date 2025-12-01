num1= input("Type first number:")
num2= input("Type second number: ")

print(f"first number is: {num1}")
print(f"second number is: {num2}")

if num1 < num2:
    print(f"{num2} comes alphatically last")

elif num1 > num2:
    print(f"{num1} comes alphatically last")

else:
    print(f"{num1} = {num2}")
    print("These are same!")
    