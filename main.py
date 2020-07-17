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


def kazanc():
    pass


def myai():
    secenek = []
    x1 = oyun_kontrol_sag_sol()
    if x1:
        secenek.append(x1)
    x2 = oyun_kontrol_yukari_asagi()
    if x2:
        secenek.append(x2)
    x3 = capraz_kontrol()
    if x3:
        secenek.append(x3)
    x4 = ortasi_bos_kontrol()
    if x4:
        secenek.append(x4)
    x5 = ortasi_bos_capraz_kontrol()
    if x5:
        secenek.append(x5)
    print("Olası hamle sayısı:", len(secenek), "Hamle:", secenek)
    if BOARD[1][1] == " ":
        BOARD[1][1] = COMP
    elif len(secenek) > 0:
        if isinstance(secenek[0], list):
            print(secenek[0])
            x1, y1 = secenek[0][0], secenek[0][1]
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


def oyun_kontrol_sag_sol():
    if BOARD[0][0] == HUMM and BOARD[0][1] == HUMM:
        if BOARD[0][2] != COMP and BOARD[0][2] != HUMM:
            return [0, 2]
    elif BOARD[0][2] == HUMM and BOARD[0][1] == HUMM:
        if BOARD[0][0] != COMP and BOARD[0][0] != HUMM:
            return [0, 0]
    elif BOARD[1][0] == HUMM and BOARD[1][1] == HUMM:
        if BOARD[1][2] != COMP and BOARD[1][2] != HUMM:
            return [1, 2]
    elif BOARD[1][2] == HUMM and BOARD[1][1] == HUMM:
        if BOARD[1][0] != COMP and BOARD[1][0] != HUMM:
            return [1, 0]
    elif BOARD[2][0] == HUMM and BOARD[2][1] == HUMM:
        if BOARD[2][2] != COMP and BOARD[2][2] != HUMM:
            return [2, 2]
    elif BOARD[2][2] == HUMM and BOARD[2][1] == HUMM:
        if BOARD[2][0] != COMP and BOARD[2][0] != HUMM:
            return [2, 0]
    else:
        return False


def oyun_kontrol_yukari_asagi():
    if BOARD[0][0] == HUMM and BOARD[1][0] == HUMM:
        if BOARD[2][0] != COMP and BOARD[2][0] != HUMM:
            return [2, 0]
    elif BOARD[2][0] == HUMM and BOARD[1][0] == HUMM:
        if BOARD[0][0] != COMP and BOARD[0][0] != HUMM:
            return [0, 0]
    elif BOARD[0][1] == HUMM and BOARD[1][1] == HUMM:
        if BOARD[2][1] != COMP and BOARD[2][1] != HUMM:
            return [2, 1]
    elif BOARD[2][1] == HUMM and BOARD[1][1] == HUMM:
        if BOARD[0][1] != COMP and BOARD[0][1] != HUMM:
            return [0, 1]
    elif BOARD[0][2] == HUMM and BOARD[1][2] == HUMM:
        if BOARD[2][2] != COMP and BOARD[2][2] != HUMM:
            return [2, 2]
    elif BOARD[2][2] == HUMM and BOARD[1][2] == HUMM:
        if BOARD[0][2] != COMP and BOARD[0][2] != HUMM:
            return [0, 2]
    else:
        return False


def capraz_kontrol():
    if BOARD[0][0] == HUMM and BOARD[1][1] == HUMM:
        if BOARD[2][2] != COMP and BOARD[2][2] != HUMM:
            return [2, 2]
    elif BOARD[2][2] == HUMM and BOARD[1][1] == HUMM:
        if BOARD[0][0] != COMP and BOARD[0][0] != HUMM:
            return [0, 0]
    elif BOARD[2][0] == HUMM and BOARD[1][1] == HUMM:
        if BOARD[0][2] != COMP and BOARD[0][2] != HUMM:
            return [0, 2]
    elif BOARD[0][2] == HUMM and BOARD[1][1] == HUMM:
        if BOARD[2][0] != COMP and BOARD[2][0] != HUMM:
            return [2, 0]
    else:
        return False


def ortasi_bos_kontrol():
    if BOARD[0][0] == HUMM and BOARD[0][2] == HUMM:
        if BOARD[0][1] != COMP and BOARD[0][1] != HUMM:
            return [0, 1]
    elif BOARD[1][0] == HUMM and BOARD[1][2] == HUMM:
        if BOARD[1][1] != COMP and BOARD[1][1] != HUMM:
            return [1, 1]
    elif BOARD[2][0] == HUMM and BOARD[2][2] == HUMM:
        if BOARD[2][1] != COMP and BOARD[2][1] != HUMM:
            return [2, 1]
    elif BOARD[0][0] == HUMM and BOARD[2][0] == HUMM:
        if BOARD[1][0] != COMP and BOARD[1][0] != HUMM:
            return [1, 0]
    elif BOARD[0][1] == HUMM and BOARD[2][1] == HUMM:
        if BOARD[1][1] != COMP and BOARD[1][1] != HUMM:
            return [1, 1]
    elif BOARD[0][2] == HUMM and BOARD[2][2] == HUMM:
        if BOARD[1][2] != COMP and BOARD[1][2] != HUMM:
            return [1, 2]
    else:
        return False


def ortasi_bos_capraz_kontrol():
    if BOARD[0][0] == HUMM and BOARD[2][2] == HUMM:
        if BOARD[1][1] != COMP and BOARD[1][1] != HUMM:
            return [1, 1]
    elif BOARD[0][2] == HUMM and BOARD[2][0] == HUMM:
        if BOARD[1][1] != COMP and BOARD[1][1] != HUMM:
            return [1, 1]
    else:
        return False


BOARD = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]


HUMM = "X"
COMP = "O"


if __name__ == "__main__":
    main()
