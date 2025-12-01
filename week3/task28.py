number = int(input("Please type a number: "))
my_flag = True

while my_flag:
    if number == 0:
        print("Kaboom!!!!")
        my_flag = False

    else:
        print(number)
        number = number - 1