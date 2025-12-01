my_flag = True
mylist = []
while my_flag:
    user_input = input("please enter an input: ")
    if user_input == "exit":
        my_flag = False
    else:
        mylist.append(user_input)
print(mylist)