num = int(input("Type a number: "))

if num > 0 and num % 2 == 0 :
    print("Your number is even")

elif num % 2 != 0 and num > 0  :
    print("Your number is odd")

elif num <= 0 :
    print("Your number is negative or zero")