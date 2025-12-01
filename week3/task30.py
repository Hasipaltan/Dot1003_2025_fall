total_number = 0
sum1 = 0
mean = 0
odd = 0
even = 0

print("dumb calculator v0.1 if you want to exit, enter 0")

my_flag = True

while my_flag:
    number = int(input("Enter a number: "))

    if number == 0:
        my_flag = False
        mean = sum1 / total_number
        print(f"Total number: {total_number}")
        print(f"Sum: {sum1}")
        print(f"Mean: {mean}")
        print(f"Odd: {odd} Even: {even}")
    
    else:
        total_number = total_number +1
        sum1 = sum1 + number

        if number % 2 == 0:
            even = even + 1

        else:
            odd = odd + 1
print("Good bye :)")