# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""


row = [0 for _ in range(5)]
board = [row.copy() for _ in range(5)]


boards = [[row.copy() for _ in range(5)] for _ in range(2)]

boards[0][0] = [1 for _ in range(5)]
boards[0][4] = [2 for _ in range(5)]
boards[1][0] = [1 for _ in range(5)]
boards[1][4] = [2 for _ in range(5)]

player = 1
def swap_number(b, x1, y1, x2, y2):
    boards[b][y1][x1], boards[b][y2][x2] = boards[b][y2][x2], boards[b][y1][x1]

def change_player(player):
    if player == 1:
        return 2
    if player == 2:
        return 1
def is_same_row_or_column(x1, y1, x2, y2):
    return (x1 - x2) * (y1 - y2) == 0
def is_movable(b, x1, y1, x2, y2):
    if is_same_row_or_column(x1, y1, x2, y2):
        if x1 == x2:
            difference = y2 - y1
            dx = 0
            dy = int(difference / abs(difference))
        else:
            difference = x2 - x1
            dx = int(difference / abs(difference))
            dy = 0
        while x1 != x2 or y1 != y2:
            x1 += dx
            y1 += dy
            if boards[b][y1][x1] != 0:
                return False
        return True
    return False
        
score_board = board.copy()

def show():
    for i in boards[0]:
        print(i)
    print()
    for i in score_board:
        print(i)
    print()
    for i in boards[1]:
        print(i)

while True:
    print("---", end="")
    command = input()
    command = command.split()
    if command[0] == "exit":
        break
    elif command[0] == "move" or command[0] == "m":
        if len(command) == 6:
            b = int(command[1])
            x1 = int(command[2])
            y1 = int(command[3])
            x2 = int(command[4])
            y2 = int(command[5])
            if boards[b][y1][x1] == player:
                if is_movable(b, x1, y1, x2, y2):
                    swap_number(b, x1, y1, x2, y2)
                    show()
                else:
                    print("you cannot move there")
            else:
                print("there is no your army")
        else:
            print("not enough values")
    elif command[0] == "show" or command[0] == "s":
        show()
    else:
        print("invaild command")