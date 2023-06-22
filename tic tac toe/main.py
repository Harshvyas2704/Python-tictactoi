
"""
minimaxing 1 player game

"""

def main():
    player1 = input("Enter Player1 name: ")
    player2 = input("Enter Player2 name: ")
    matrix = []
    matrix = createMatrix(matrix)
    gamePlay(player1, player2, matrix)


def createMatrix(matrix):
    row1 = ["0", "1", "2"]
    row2 = ["3", "4", "5"]
    row3 = ["6", "7", "8"]
    matrix.append(row1)
    matrix.append(row2)
    matrix.append(row3)
    return matrix


def matrix_append(matrix, n, k):
    match n:
        case 0:
            matrix[0][0] = k
        case 1:
            matrix[0][1] = k
        case 2:
            matrix[0][2] = k
        case 3:
            matrix[1][0] = k
        case 4:
            matrix[1][1] = k
        case 5:
            matrix[1][2] = k
        case 6:
            matrix[2][0] = k
        case 7:
            matrix[2][1] = k
        case 8:
            matrix[2][2] = k
    return


def checkForWinner(matrix, k):
    # Check for Row
    for i in range(len(matrix)):
        count = 0
        for j in range(len(matrix[0])):
            if matrix[i][j] == k:
                count += 1

        if count == 3:
            return True

    # Check for Column
    for i in range(len(matrix)):
        count = 0
        for j in range(len(matrix[0])):
            if matrix[j][i] == k:
                count += 1

        if count == 3:
            return True

    # Check for left diagonal
    count = 0
    for i in range(len(matrix)):
        if matrix[i][i] == k:
            count += 1

    if count == 3:
        return True

    # Check for right diagonal

    left = len(matrix) - 1
    right = 0
    count = 0
    for i in range(len(matrix)):
        if matrix[right][left] == k:
            count += 1
        left -= 1
        right += 1

    if count == 3:
        return True

    return False


def gamePlay(player1, player2, matrix):

    addresses = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    counter = 1

    while counter < 10:

        if counter % 2 != 0:
            print(f"You can choose from this places: ")

            for x in matrix:
                print(x)

            flag = True
            while flag:
                player1_choice = int(input(f"{player1} your turn: "))
                if player1_choice > 8 or player1_choice < 0:
                    print(f"Choose valid number you idiot {player1}!!!")
                    continue
                else:
                    flag = False

            matrix_append(matrix, player1_choice, "X")
            addresses.remove(player1_choice)

            if checkForWinner(matrix, "X"):

                print(f"{player1} is winner!!")
                for x in matrix:
                    print(x)

                return

        else:
            print(f"You can choose from this places: ")

            for x in matrix:
                print(x)
            flag = True
            while flag:
                player2_choice = int(input(f"{player2} your turn: "))
                if player2_choice > 8 or player2_choice < 0:
                    print(f"Choose valid number you idiot!!! {player2}")
                    continue
                else:
                    flag = False
            matrix_append(matrix, player2_choice, "O")
            addresses.remove(player2_choice)

            if checkForWinner(matrix, "O"):

                print(f"{player2} is winner!!")
                for x in matrix:
                    print(x)
                    
                return

        counter += 1
        if counter == 10:
            print("Match draw!!!")
            return


main()