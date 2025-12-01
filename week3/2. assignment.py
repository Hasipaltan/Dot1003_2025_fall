def start_adventure():
    print("Welcome to the simple adventure game!")
    user_input = input("Please make a choice -> idle, left, right: ")

def left():
    print("Its a sand worm, you wanna fight?")

def right():
    print("You find a magical chest!")

def idle():
    print("HAHAHAH HOW SCARED YOU ARE!!")
    print("You're boring:(")

    if user_input == "left":
        left()
    elif user_input == "right":
        right()
    elif user_input == "idle":
        idle()
    else:
        print("invalid Input")
        start_adventure()

if __name__ == "__main__":
    start_adventure()