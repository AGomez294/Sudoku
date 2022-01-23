grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]


def printGrid():
    for x in range(9):
        for y in range(9):
            print(grid[x][y], end="")
            if y == 2 or y == 5 or y == 8:
                print(" ", end="")
        print()
        if x == 2 or x == 5:
            print()


def check(value, x, y):
    if 0 <= x <= 2:
        if 0 <= y <= 2:
            for i in range(3):
                for n in range(3):
                    if x != i and y != n:
                        if grid[i][n] == value:
                            return False
        if 3 <= y <= 5:
            for i in range(3):
                for n in range(3, 6):
                    if x != i and y != n:
                        if grid[i][n] == value:
                            return False
        if 6 <= y <= 9:
            for i in range(3):
                for n in range(6, 9):
                    if x != i and y != n:
                        if grid[i][n] == value:
                            return False
    if 3 <= x <= 5:
        if 0 <= y <= 2:
            for i in range(3, 6):
                for n in range(3):
                    if x != i and y != n:
                        if grid[i][n] == value:
                            return False
        if 3 <= y <= 5:
            for i in range(3, 6):
                for n in range(3, 6):
                    if x != i and y != n:
                        if grid[i][n] == value:
                            return False
        if 6 <= y <= 9:
            for i in range(3, 6):
                for n in range(6, 9):
                    if x != i and y != n:
                        if grid[i][n] == value:
                            return False
    if 6 <= x <= 9:
        if 0 <= y <= 2:
            for i in range(6, 9):
                for n in range(3):
                    if x != i and y != n:
                        if grid[i][n] == value:
                            return False
        if 3 <= y <= 5:
            for i in range(6, 9):
                for n in range(3, 6):
                    if x != i and y != n:
                        if grid[i][n] == value:
                            return False
        if 6 <= y <= 9:
            for i in range(6, 9):
                for n in range(6, 9):
                    if x != i and y != n:
                        if grid[i][n] == value:
                            return False
    for i in range(9):
        if y != i:
            if grid[x][i] == value:
                return False
        if x != i:
            if grid[i][y] == value:
                return False
    return True


def solve():
    a = b = 0
    while a != 9:
        while b != 9:
            if grid[a][b] == 0:
                grid[a][b] += 1
            if check(grid[a][b], a, b):
                b += 1
            else:
                grid[a][b] += 1
                if grid[a][b] == 10:
                    while a != -1:
                        grid[a][b] = 0
                        b -= 1
                        if b < 0:
                            b = 8
                            a -= 1
                        grid[a][b] += 1
                        if grid[a][b] != 10:
                            break

        b = 0
        a += 1


def userStuff():
    q1 = input("Welcome to Sudoku Solutions, in order to edit the grid, press \"1\", otherwise to continue with the "
               "\nbase demonstration, press \"0\" ")
    q1 = int(q1)
    while q1 != 1 or q1 != 0:

        if q1 == 1:
            print("Numbers are organized by rows and columns, x and y respectively. In order to change a certain "
                  "cell for example, one on the first row, third column, type \"31\". Type \"DONE\" in all CAPS if "
                  "done and \"P\" in all CAPS to check out a preview of the sudoku grid")
            q2 = input("What cell do you want to insert a value in?")
            while q2 != "DONE":
                if q2 == "P":
                    printGrid()
                    q2 = input("Continue?")
                elif q2.isnumeric():
                    x = q2[:1]
                    y = q2[1:2]
                    x = int(x) - 1
                    y = int(y) - 1
                    q3 = input("Change this cell to what value?")
                    while not q3.isnumeric():
                        q3 = input("Error, value needs to be an integer")
                    q3 = int(q3)
                    while q3 < 0 or q3 > 9:
                        q3 = input("Error, value needs to be between 0-9")
                    grid[x][y] = q3
                    q2 = input("Continue to another cell?")
                else:
                    q2 = input("Error, try again")

            break
        elif q1 == 0:
            break
        else:
            q1 = input("Welcome to Sudoku Solutions, in order to edit the grid, press \"1\", otherwise to continue "
                       "with the \nbase demonstration, press \"0\" ")
            q1 = int(q1)


userStuff()
solve()
print("Here:")
printGrid()
