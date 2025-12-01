sentence = "The quick brown fox jumps over the lazy dog."
my_flag = True

while my_flag:
    input1 = input("What are you looking for? ")

    if input1 == "-1":
        print("Bye.")
        my_flag = False

    location = sentence.find(input1)

    if location != -1:
        print(f"found it at {location}")
    else:
        print("not found")