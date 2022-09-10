def drawField(field):
    for row in range(5):
        if row % 2 == 0:
            boardRow = int(row / 2)
            for column in range(5):
                if column % 2 == 0:
                    boardColumn = int(column / 2)
                    if not column == 4:
                        print(field[boardColumn][boardRow], end="")
                    else:
                        print(field[boardColumn][boardRow])
                else:
                    print("|", end="")
        else:
            print("-----")


Player = 1
currentFiled = [[" "," "," "],[" "," "," "],[" "," "," "]]
drawField(currentFiled)
while(True):
    print("Players turn: ", Player)
    MoveRow = int(input("Please enter the row: "))
    MoveColumn = int(input("Please enter the column: "))
    if Player == 1:
        # Make a Move for player 1
        if currentFiled[MoveColumn][MoveRow] == " ":
            currentFiled[MoveColumn][MoveRow] = "X"
            Player = 2
    else:
        # Make a Move for player 2
        if currentFiled[MoveColumn][MoveRow] == " ":
            currentFiled[MoveColumn][MoveRow] = "O"
            Player = 1
    drawField(currentFiled)



