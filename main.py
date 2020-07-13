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
    myai()
    # ai çalışıyor.
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
    toplam = 0
    while 1:
        x, y = random.randint(0, 2), random.randint(0, 2)
        if kontrol(x, y):
            BOARD[x][y] = "O"
            break
        else:
            toplam += 1
            if toplam == 9:
                break


BOARD = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

HUMM = "X"
COMP = "O"


if __name__ == "__main__":
    main()
