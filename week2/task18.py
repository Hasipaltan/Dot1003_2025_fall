num = int(input("Type a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")

elif num % 5 == 0:
    print("buzz")

elif num % 3 == 0:
    print("fizz")