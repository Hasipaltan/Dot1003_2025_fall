game_list = []
my_flag = True

while my_flag:
    game = input("Type a game name: ")

    if game == "exit":
        my_flag = False
    else:
        game_list.append(game)

def anarya(liste):

    ters = []
    for i in range(len(liste)-1, -1, -1):
        ters.append(liste[i])
    return ters

print(game_list)
print(anarya(game_list))