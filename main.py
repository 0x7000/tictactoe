#!/usr/bin/env python
import random


def main():
    sira = 0
    # boş oyun alanı hazırlanıyor.

    #   1   2   3
    #   4   5   6
    #   7   8   9

    BOARD[0][0], BOARD[0][1], BOARD[0][2] = " ", " ", " "
    BOARD[1][0], BOARD[1][1], BOARD[1][2] = " ", " ", " "
    BOARD[2][0], BOARD[2][1], BOARD[2][2] = " ", " ", " "
    # tahta ekrana basıldı.
    tahta()
    # giriş
    while 1:
        giris = input(":")
        if giris == "1":
            if kontrol(0, 0):
                BOARD[0][0] = HUMM
                sira = 1
        elif giris == "2":
            if kontrol(0, 1):
                BOARD[0][1] = HUMM
                sira = 1
        elif giris == "3":
            if kontrol(0, 2):
                BOARD[0][2] = HUMM
                sira = 1
        elif giris == "4":
            if kontrol(1, 0):
                BOARD[1][0] = HUMM
                sira = 1
        elif giris == "5":
            if kontrol(1, 1):
                BOARD[1][1] = HUMM
                sira = 1
        elif giris == "6":
            if kontrol(1, 2):
                BOARD[1][2] = HUMM
                sira = 1
        elif giris == "7":
            if kontrol(2, 0):
                BOARD[2][0] = HUMM
                sira = 1
        elif giris == "8":
            if kontrol(2, 1):
                BOARD[2][1] = HUMM
                sira = 1
        elif giris == "9":
            if kontrol(2, 2):
                BOARD[2][2] = HUMM
                sira = 1
        elif giris == "q":
            break
        else:
            pass
        if sira == 1:
            myai()
            sira = 0
        tahta()


def tahta():
    for x in BOARD:
        print(x)


def kontrol(x, y):
    if BOARD[x][y] == HUMM or BOARD[x][y] == COMP:
        return False
    else:
        return True


def myai():
    turn = True
    #  sağ sol kontrol
    if BOARD[0][0] == "X" and BOARD[0][1] == "X":
        if BOARD[0][2] != "O" and BOARD[0][2] != "X":
            if turn:
                BOARD[0][2] = "O"
                turn = False
    if BOARD[0][2] == "X" and BOARD[0][1] == "X":
        if BOARD[0][0] != "O" and BOARD[0][0] != "X":
            if turn:
                BOARD[0][0] = "O"
                turn = False
    if BOARD[1][0] == "X" and BOARD[1][1] == "X":
        if BOARD[1][2] != "O" and BOARD[1][2] != "X":
            if turn:
                BOARD[1][2] = "O"
                turn = False
    if BOARD[1][2] == "X" and BOARD[1][1] == "X":
        if BOARD[1][0] != "O" and BOARD[1][0] != "X":
            if turn:
                BOARD[1][0] = "O"
                turn = False
    if BOARD[2][0] == "X" and BOARD[2][1] == "X":
        if BOARD[2][2] != "O" and BOARD[2][2] != "X":
            if turn:
                BOARD[2][2] = "O"
                turn = False
    if BOARD[2][2] == "X" and BOARD[2][1] == "X":
        if BOARD[2][0] != "O" and BOARD[2][0] != "X":
            if turn:
                BOARD[2][0] = "O"
                turn = False
    #  yukarı aşağı kontrol
    if BOARD[0][0] == "X" and BOARD[1][0] == "X":
        if BOARD[2][0] != "O" and BOARD[2][0] != "X":
            if turn:
                BOARD[2][0] = "O"
                turn = False
    if BOARD[2][0] == "X" and BOARD[1][0] == "X":
        if BOARD[0][0] != "O" and BOARD[0][0] != "X":
            if turn:
                BOARD[0][0] = "O"
                turn = False
    if BOARD[0][1] == "X" and BOARD[1][1] == "X":
        if BOARD[2][1] != "O" and BOARD[2][1] != "X":
            if turn:
                BOARD[2][1] = "O"
                turn = False
    if BOARD[2][1] == "X" and BOARD[1][1] == "X":
        if BOARD[0][1] != "O" and BOARD[0][1] != "X":
            if turn:
                BOARD[0][1] = "O"
                turn = False
    if BOARD[0][2] == "X" and BOARD[1][2] == "X":
        if BOARD[2][2] != "O" and BOARD[2][2] != "X":
            if turn:
                BOARD[2][2] = "O"
                turn = False
    if BOARD[2][2] == "X" and BOARD[1][2] == "X":
        if BOARD[0][2] != "O" and BOARD[0][2] != "X":
            if turn:
                BOARD[0][2] = "O"
                turn = False
    #  çarpraz kontrol
    if BOARD[0][0] == "X" and BOARD[1][1] == "X":
        if BOARD[2][2] != "O" and BOARD[2][2] != "X":
            if turn:
                BOARD[2][2] = "O"
                turn = False
    if BOARD[2][2] == "X" and BOARD[1][1] == "X":
        if BOARD[0][0] != "O" and BOARD[0][0] != "X":
            if turn:
                BOARD[0][0] = "O"
                turn = False
    if BOARD[2][0] == "X" and BOARD[1][1] == "X":
        if BOARD[0][2] != "O" and BOARD[0][2] != "X":
            if turn:
                BOARD[0][2] = "O"
                turn = False
    if BOARD[0][2] == "X" and BOARD[1][1] == "X":
        if BOARD[2][0] != "O" and BOARD[2][0] != "X":
            if turn:
                BOARD[2][0] = "O"
                turn = False
    #  ortası boş kontrol
    if BOARD[0][0] == "X" and BOARD[0][2] == "X":
        if BOARD[0][1] != "O" and BOARD[0][1] != "X":
            if turn:
                BOARD[0][1] = "O"
                turn = False
    if BOARD[1][0] == "X" and BOARD[1][2] == "X":
        if BOARD[1][1] != "O" and BOARD[1][1] != "X":
            if turn:
                BOARD[1][1] = "O"
                turn = False
    if BOARD[2][0] == "X" and BOARD[2][2] == "X":
        if BOARD[2][1] != "O" and BOARD[2][1] != "X":
            if turn:
                BOARD[2][1] = "O"
                turn = False
    if BOARD[0][0] == "X" and BOARD[2][0] == "X":
        if BOARD[1][0] != "O" and BOARD[1][0] != "X":
            if turn:
                BOARD[1][0] = "O"
                turn = False
    if BOARD[0][1] == "X" and BOARD[2][1] == "X":
        if BOARD[1][1] != "O" and BOARD[1][1] != "X":
            if turn:
                BOARD[1][1] = "O"
                turn = False
    if BOARD[0][2] == "X" and BOARD[2][2] == "X":
        if BOARD[1][2] != "O" and BOARD[1][2] != "X":
            if turn:
                BOARD[1][2] = "O"
                turn = False
    # ortası boş çarpaz kontrol
    if BOARD[0][0] == "X" and BOARD[2][2] == "X":
        if BOARD[1][1] != "O" and BOARD[1][1] != "X":
            if turn:
                BOARD[1][1] = "O"
                turn = False
    if BOARD[0][2] == "X" and BOARD[2][0] == "X":
        if BOARD[1][1] != "O" and BOARD[1][1] != "X":
            if turn:
                BOARD[1][1] = "O"
                turn = False
    if turn:
        x, y = random.randint(0, 2), random.randint(0, 2)
        if kontrol(x, y):
            BOARD[x][y] = "O"


BOARD = [["0", "1", "2"],
         ["0", "1", "2"],
         ["0", "1", "2"]]

HUMM = "X"
COMP = "O"


if __name__ == "__main__":
    main()
