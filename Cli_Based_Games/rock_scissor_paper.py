from random import randint
game = {
    "R": 1,
    "S": 2,
    "P": 3
}

print("Let's Play A Rock-Scissor-Paper Game")

n = int(input("How many times you want to play this game = "))

for i in range(1, n+1):

    print("Press R for ROCK , S for SCISSOR ,P for Paper")
    z = game.get(input("R/S/P : ").upper())
    y = randint(1, 3)
    print("\n")
    if z == 1:
        print("PLAYER: ROCK")
    if z == 2:
        print("PLAYER: SCISSOR")
    if z == 3:
        print("PLAYER: PAPER")
    if y == 1:
        print("Computer: ROCK")
    if y == 2:
        print("Computer: SCISSOR")
    if y == 3:
        print("Computer: PAPER")
    if z == y:
        print("IT's A DRAW")
    if z == int(1) and y == int(2):
        print("Player Won")
        print("Congrats!!!!")
    elif z == 1 and y == 3:
        print("Oops!!")
        print("Player Lose")
        print("Better Luck Next Time!")
    elif z == 2 and y == 1:
        print("Oops!!")
        print("Player Lose")
        print("Better Luck Next Time!")
    elif z == 2 and y == 3:
        print("Player Won")
        print("Congrats!!!!")
    elif z == 3 and y == 1:
        print("Player Won")
        print("Congrats!!!!")
    elif z == 3 and y == 2:
        print("Oops!!")
        print("Player Lose")
        print("Better Luck Next Time!")


print("\n")

input("Press enter to exit ;)")
