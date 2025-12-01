my_flag = True
number = 3
main_password = "487042"

while my_flag:
    password = input("Password: ")
    number = number - 1

    if number == 0:
        print("Incorrect Password. Exterminate...")
        my_flag = False

    elif password == main_password:
        print("Welcome")
        my_flag = False
    