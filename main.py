#!/usr/bin/env python


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
    # giriş
    myai()
    tahta()
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
    deger = oyun_kontrol()
    if isinstance(deger, list):
        x1, y1 = deger[0], deger[1]
        BOARD[x1][y1] = COMP
    else:
        turn = True
        for x in range(3):
            for y in range(3):
                if BOARD[x][y] == " ":
                    BOARD[x][y] = COMP
                    turn = False
                    break
            if not turn:
                break


def oyun_kontrol():
    #  sağ sol kontrol
    if BOARD[0][0] == "X" and BOARD[0][1] == "X":
        if BOARD[0][2] != "O" and BOARD[0][2] != "X":
            return [0, 2]
    if BOARD[0][2] == "X" and BOARD[0][1] == "X":
        if BOARD[0][0] != "O" and BOARD[0][0] != "X":
            return [0, 0]
    if BOARD[1][0] == "X" and BOARD[1][1] == "X":
        if BOARD[1][2] != "O" and BOARD[1][2] != "X":
            return [1, 2]
    if BOARD[1][2] == "X" and BOARD[1][1] == "X":
        if BOARD[1][0] != "O" and BOARD[1][0] != "X":
            return [1, 0]
    if BOARD[2][0] == "X" and BOARD[2][1] == "X":
        if BOARD[2][2] != "O" and BOARD[2][2] != "X":
            return [2, 2]
    if BOARD[2][2] == "X" and BOARD[2][1] == "X":
        if BOARD[2][0] != "O" and BOARD[2][0] != "X":
            return [2, 0]
    #  yukarı aşağı kontrol
    if BOARD[0][0] == "X" and BOARD[1][0] == "X":
        if BOARD[2][0] != "O" and BOARD[2][0] != "X":
            return [2, 0]
    if BOARD[2][0] == "X" and BOARD[1][0] == "X":
        if BOARD[0][0] != "O" and BOARD[0][0] != "X":
            return [0, 0]
    if BOARD[0][1] == "X" and BOARD[1][1] == "X":
        if BOARD[2][1] != "O" and BOARD[2][1] != "X":
            return [2, 1]
    if BOARD[2][1] == "X" and BOARD[1][1] == "X":
        if BOARD[0][1] != "O" and BOARD[0][1] != "X":
            return [0, 1]
    if BOARD[0][2] == "X" and BOARD[1][2] == "X":
        if BOARD[2][2] != "O" and BOARD[2][2] != "X":
            return [2, 2]
    if BOARD[2][2] == "X" and BOARD[1][2] == "X":
        if BOARD[0][2] != "O" and BOARD[0][2] != "X":
            return [0, 2]
    #  çarpraz kontrol
    if BOARD[0][0] == "X" and BOARD[1][1] == "X":
        if BOARD[2][2] != "O" and BOARD[2][2] != "X":
            return [2, 2]
    if BOARD[2][2] == "X" and BOARD[1][1] == "X":
        if BOARD[0][0] != "O" and BOARD[0][0] != "X":
            return [0, 0]
    if BOARD[2][0] == "X" and BOARD[1][1] == "X":
        if BOARD[0][2] != "O" and BOARD[0][2] != "X":
            return [0, 2]
    if BOARD[0][2] == "X" and BOARD[1][1] == "X":
        if BOARD[2][0] != "O" and BOARD[2][0] != "X":
            return [2, 0]
    #  ortası boş kontrol
    if BOARD[0][0] == "X" and BOARD[0][2] == "X":
        if BOARD[0][1] != "O" and BOARD[0][1] != "X":
            return [0, 1]
    if BOARD[1][0] == "X" and BOARD[1][2] == "X":
        if BOARD[1][1] != "O" and BOARD[1][1] != "X":
            return [1, 1]
    if BOARD[2][0] == "X" and BOARD[2][2] == "X":
        if BOARD[2][1] != "O" and BOARD[2][1] != "X":
            return [2, 1]
    if BOARD[0][0] == "X" and BOARD[2][0] == "X":
        if BOARD[1][0] != "O" and BOARD[1][0] != "X":
            return [1, 0]
    if BOARD[0][1] == "X" and BOARD[2][1] == "X":
        if BOARD[1][1] != "O" and BOARD[1][1] != "X":
            return [1, 1]
    if BOARD[0][2] == "X" and BOARD[2][2] == "X":
        if BOARD[1][2] != "O" and BOARD[1][2] != "X":
            return [1, 2]
    # ortası boş çarpaz kontrol
    if BOARD[0][0] == "X" and BOARD[2][2] == "X":
        if BOARD[1][1] != "O" and BOARD[1][1] != "X":
            return [1, 1]
    if BOARD[0][2] == "X" and BOARD[2][0] == "X":
        if BOARD[1][1] != "O" and BOARD[1][1] != "X":
            return [1, 1]


BOARD = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

HUMM = "X"
COMP = "O"


if __name__ == "__main__":
    main()
