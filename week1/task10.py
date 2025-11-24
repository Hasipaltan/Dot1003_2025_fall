time = int(input("How many times a week do you eat at the student cafeteria? "))
price = int(input("The price of a typical student lunch? "))
money = int(input("How much money do you spend on groceries in a week? "))

print("Average food expenditure:")
print(f"Daily: {time / 7 * price + money / 7}")
print(f"Weekly: {time * price + money}")
print(f"Monthly: {(time / 7 * price + money / 7) * 30}")