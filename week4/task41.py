def words(arg1, arg2):
    if arg1 > arg2:
        return arg1
    elif arg2 > arg1 :
        return arg1
    else:
        print("Their leght are smame")
        return arg1
user_input = input("First word: ")
user_input2 = input("Second word: ")
last = words(user_input,user_input2)
print(last)