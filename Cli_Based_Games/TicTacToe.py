from copy import deepcopy

def display(mat):
    print(
    f"   {mat[0][0]}  |  {mat[0][1]}  |  {mat[0][2]}\n",
    f"------------------\n"
    f"   {mat[1][0]}  |  {mat[1][1]}  |  {mat[1][2]}\n",
    f"------------------\n"
    f"   {mat[2][0]}  |  {mat[2][1]}  |  {mat[2][2]}\n"    
    )

def win(mat):
    # check row
    first_row = mat[0][0] == mat[0][1] and mat[0][0] == mat[0][2] and mat[0][0] != " "
    second_row = mat[1][0] == mat[1][1] and mat[1][0] == mat[1][2] and mat[1][0] != " "
    third_row = mat[2][0] == mat[2][1] and mat[2][0] == mat[2][2] and mat[2][0] != " "
    if first_row:
        return mat[0][0]
    elif second_row:
        return mat[1][0]
    elif third_row:
        return mat[2][0]

    # check col
    first_col = mat[0][0] == mat[1][0] and mat[0][0] == mat[2][0] and mat[0][0] != " "
    second_col = mat[0][1] == mat[1][1] and mat[0][1] == mat[2][1] and mat[0][1] != " "
    third_col = mat[0][2] == mat[1][2] and mat[0][2] == mat[2][2] and mat[0][2] != " "
    if first_col:
        return mat[0][0]
    elif second_col:
        return mat[0][1]
    elif third_col:
        return mat[0][2]

    # check diagonal
    if mat[0][0] == mat[1][1] and mat[0][0] == mat[2][2] and mat[0][0] != " ":
        return mat[0][0]
    elif mat[0][2] == mat[1][1] and mat[0][2] == mat[2][0] and mat[0][2] != " ":
        return mat[0][2]

    return False

def full(mat):
    for i in range(3):
        for j in range(3):
            if mat[i][j] == " ":
                return False
    return True

def compMove(mat):
    tryMat = deepcopy(mat)
    for i in range(3):
        for j in range(3):
            if tryMat[i][j] == " ":
                tryMat[i][j] = "O"
                if win(tryMat) == "O":
                    return [i, j]
                tryMat[i][j] = " "

    for i in range(3):
        for j in range(3):
            if tryMat[i][j] == " ":
                tryMat[i][j] = "X"
                if win(tryMat) == "X":
                    return [i, j]
                tryMat[i][j] = " "

    for i in range(3):
        for j in range(3):
            if tryMat[i][j] == " ":
                return [i, j]
def main(mat):
    while True:
        while True:
            while True:
                try:
                    row = int(input("Please enter row number (1 to 3) "))
                except ValueError:
                    print("Please enter a valid value")
                    continue

                if row < 1 or row > 3:
                    print("Please enter a value between 1 and 3")
                else:
                    break            

            while True:
                try:
                    col = int(input("Please enter col number (1 to 3) "))
                except ValueError:
                    print("Please enter a valid value")
                    continue

                if col < 1 or col > 3:
                    print("Please enter a value between 1 and 3")
                else:
                    break

            row -= 1
            col -= 1
            if mat[row][col] != " ":
                print("Please pick an empty position")
            else:
                break

        mat[row][col] = "X"
        display(mat)
        if win(mat) == "X":
            print("Congratulation! You win!")
            break
        elif full(mat):
            print("It's a tie!")
            break

        row, col = compMove(mat)
        mat[row][col] = "O"
        display(mat)
        if win(mat) == "O":
            print("Oh no! You lose!")
            break
        elif full(mat):
            print("It's a tie!")
            break

if __name__ == "__main__":
    mat = [[" " for i in range(3)] for j in range(3)]
    print("Welcome to Tic Tac Toe game!")
    print("You will play as X")
    main(mat)