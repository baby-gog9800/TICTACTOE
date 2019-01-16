import tictactoeiteration1lvl
a = tictactoeiteration1lvl.Game()
print("X or O")
x=input()
if x == "X":
    a.user_sign = "X"
else:
    a.user_sign = "O"

print("Wanna play first.. (type \'yes\' or \'no\')")
get_input = input()
if get_input == "yes":
    a.display()
    while True:
        if a.winner == None:
            a.user_play()
        if a.winner == None:
            a.cpu_play()
        else:
            break
    print("Game Ends..! Congratulations to %s i.e. our winner" % a.winner)
else:
    while True :
        if a.winner == None:
            a.cpu_play()
        if a.winner == None:
            a.user_play()
        else:
            break
    print("Game Ends..! Congratulations to %s i.e. our winner" % a.winner)

