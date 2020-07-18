#!/usr/bin/env python


def main():
    sira = 0
    beraber = False
    # boş oyun alanı hazırlanıyor.

    #   1   2   3
    #   4   5   6
    #   7   8   9

    BOARD[0][0], BOARD[0][1], BOARD[0][2] = " ", " ", " "
    BOARD[1][0], BOARD[1][1], BOARD[1][2] = " ", " ", " "
    BOARD[2][0], BOARD[2][1], BOARD[2][2] = " ", " ", " "
    # tahta ekrana basıldı.
    # giriş
    tahta()
    while not beraber:
        say = 9
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
        for x in range(3):
            for y in range(3):
                if BOARD[x][y] != " ":
                    say -= 1
            if say == 0:
                print("Berabere.")
                beraber = True
        tahta()
        bitti = bitti_comp()
        bitti2 = bitti_humm()
        if bitti:
            print("Bilgisayar Kazandı.")
            break
        if bitti2:
            print("kullanıcı Kazandı.")
            break


def tahta():
    for x in BOARD:
        print(x)


def kontrol(x, y):
    if BOARD[x][y] == HUMM or BOARD[x][y] == COMP:
        return False
    else:
        return True


def kazanc():
    secenek = []
    x1 = oyun_kontrol_sag_sol_comp()
    if x1:
        secenek.append(x1)
    x2 = oyun_kontrol_yukari_asagi_comp()
    if x2:
        secenek.append(x2)
    x3 = capraz_kontrol_comp()
    if x3:
        secenek.append(x3)
    x4 = ortasi_bos_kontrol_comp()
    if x4:
        secenek.append(x4)
    x5 = ortasi_bos_capraz_kontrol_comp()
    if x5:
        secenek.append(x5)
    if len(secenek) == 1:
        print("kazandıran hamle sayısı:", len(secenek), "Hamle:", secenek)
        if isinstance(secenek[0], list):
            print("Kazandıran seçenek", secenek[0])
            return secenek[0]
        else:
            return False


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
    print("Karşı hamle sayısı:", len(secenek), "Hamle:", secenek)
    hamle = kazanc()
    if BOARD[1][1] == " ":
        BOARD[1][1] = COMP
    elif isinstance(hamle, list):
        k1, l1 = hamle[0], hamle[1]
        BOARD[k1][l1] = COMP
    elif len(secenek) > 0:
        for xx in secenek:
            if isinstance(xx, list):
                xx1, yy1 = xx[0], xx[1]
                if kontrol(xx1, yy1):
                    BOARD[xx1][yy1] = COMP
                    break
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


def bitti_comp():
    if BOARD[0][0] == COMP:
        if BOARD[0][1] == COMP:
            if BOARD[0][2] == COMP:
                print("ok")
                return True
    if BOARD[1][0] == COMP:
        if BOARD[1][1] == COMP:
            if BOARD[1][2] == COMP:
                print("ok")
                return True
    if BOARD[2][0] == COMP:
        if BOARD[2][1] == COMP:
            if BOARD[2][2] == COMP:
                print("ok")
                return True
    if BOARD[0][0] == COMP:
        if BOARD[1][0] == COMP:
            if BOARD[2][0] == COMP:
                print("ok")
                return True
    if BOARD[0][1] == COMP:
        if BOARD[1][1] == COMP:
            if BOARD[2][1] == COMP:
                print("ok")
                return True
    if BOARD[0][2] == COMP:
        if BOARD[1][2] == COMP:
            if BOARD[2][2] == COMP:
                print("ok")
                return True
    if BOARD[0][0] == COMP:
        if BOARD[1][1] == COMP:
            if BOARD[2][2] == COMP:
                print("ok")
                return True
    if BOARD[0][2] == COMP:
        if BOARD[1][1] == COMP:
            if BOARD[2][0] == COMP:
                print("ok")
                return True


def bitti_humm():
    if BOARD[0][0] == HUMM:
        if BOARD[0][1] == HUMM:
            if BOARD[0][2] == HUMM:
                print("ok")
                return True
    if BOARD[1][0] == HUMM:
        if BOARD[1][1] == HUMM:
            if BOARD[1][2] == HUMM:
                print("ok")
                return True
    if BOARD[2][0] == HUMM:
        if BOARD[2][1] == HUMM:
            if BOARD[2][2] == HUMM:
                print("ok")
                return True
    if BOARD[0][0] == HUMM:
        if BOARD[1][0] == HUMM:
            if BOARD[2][0] == HUMM:
                print("ok")
                return True
    if BOARD[0][1] == HUMM:
        if BOARD[1][1] == HUMM:
            if BOARD[2][1] == HUMM:
                print("ok")
                return True
    if BOARD[0][2] == HUMM:
        if BOARD[1][2] == HUMM:
            if BOARD[2][2] == HUMM:
                print("ok")
                return True
    if BOARD[0][0] == HUMM:
        if BOARD[1][1] == HUMM:
            if BOARD[2][2] == HUMM:
                print("ok")
                return True
    if BOARD[0][2] == HUMM:
        if BOARD[1][1] == HUMM:
            if BOARD[2][0] == HUMM:
                print("ok")
                return True


def oyun_kontrol_sag_sol():
    if BOARD[0][0] == HUMM and BOARD[0][1] == HUMM:
        if BOARD[0][2] != COMP and BOARD[0][2] != HUMM:
            return [0, 2]
    if BOARD[0][2] == HUMM and BOARD[0][1] == HUMM:
        if BOARD[0][0] != COMP and BOARD[0][0] != HUMM:
            return [0, 0]
    if BOARD[1][0] == HUMM and BOARD[1][1] == HUMM:
        if BOARD[1][2] != COMP and BOARD[1][2] != HUMM:
            return [1, 2]
    if BOARD[1][2] == HUMM and BOARD[1][1] == HUMM:
        if BOARD[1][0] != COMP and BOARD[1][0] != HUMM:
            return [1, 0]
    if BOARD[2][0] == HUMM and BOARD[2][1] == HUMM:
        if BOARD[2][2] != COMP and BOARD[2][2] != HUMM:
            return [2, 2]
    if BOARD[2][2] == HUMM and BOARD[2][1] == HUMM:
        if BOARD[2][0] != COMP and BOARD[2][0] != HUMM:
            return [2, 0]


def oyun_kontrol_sag_sol_comp():
    if BOARD[0][0] == COMP and BOARD[0][1] == COMP:
        if BOARD[0][2] != HUMM and BOARD[0][2] != COMP:
            return [0, 2]
    if BOARD[0][2] == COMP and BOARD[0][1] == COMP:
        if BOARD[0][0] != HUMM and BOARD[0][0] != COMP:
            return [0, 0]
    if BOARD[1][0] == COMP and BOARD[1][1] == COMP:
        if BOARD[1][2] != HUMM and BOARD[1][2] != COMP:
            return [1, 2]
    if BOARD[1][2] == COMP and BOARD[1][1] == COMP:
        if BOARD[1][0] != HUMM and BOARD[1][0] != COMP:
            return [1, 0]
    if BOARD[2][0] == COMP and BOARD[2][1] == COMP:
        if BOARD[2][2] != HUMM and BOARD[2][2] != COMP:
            return [2, 2]
    if BOARD[2][2] == COMP and BOARD[2][1] == COMP:
        if BOARD[2][0] != HUMM and BOARD[2][0] != COMP:
            return [2, 0]


def oyun_kontrol_yukari_asagi():
    if BOARD[0][0] == HUMM and BOARD[1][0] == HUMM:
        if BOARD[2][0] != COMP and BOARD[2][0] != HUMM:
            return [2, 0]
    if BOARD[2][0] == HUMM and BOARD[1][0] == HUMM:
        if BOARD[0][0] != COMP and BOARD[0][0] != HUMM:
            return [0, 0]
    if BOARD[0][1] == HUMM and BOARD[1][1] == HUMM:
        if BOARD[2][1] != COMP and BOARD[2][1] != HUMM:
            return [2, 1]
    if BOARD[2][1] == HUMM and BOARD[1][1] == HUMM:
        if BOARD[0][1] != COMP and BOARD[0][1] != HUMM:
            return [0, 1]
    if BOARD[0][2] == HUMM and BOARD[1][2] == HUMM:
        if BOARD[2][2] != COMP and BOARD[2][2] != HUMM:
            return [2, 2]
    if BOARD[2][2] == HUMM and BOARD[1][2] == HUMM:
        if BOARD[0][2] != COMP and BOARD[0][2] != HUMM:
            return [0, 2]


def oyun_kontrol_yukari_asagi_comp():
    if BOARD[0][0] == COMP and BOARD[1][0] == COMP:
        if BOARD[2][0] != HUMM and BOARD[2][0] != COMP:
            return [2, 0]
    if BOARD[2][0] == COMP and BOARD[1][0] == COMP:
        if BOARD[0][0] != HUMM and BOARD[0][0] != COMP:
            return [0, 0]
    if BOARD[0][1] == COMP and BOARD[1][1] == COMP:
        if BOARD[2][1] != HUMM and BOARD[2][1] != COMP:
            return [2, 1]
    if BOARD[2][1] == COMP and BOARD[1][1] == COMP:
        if BOARD[0][1] != HUMM and BOARD[0][1] != COMP:
            return [0, 1]
    if BOARD[0][2] == COMP and BOARD[1][2] == COMP:
        if BOARD[2][2] != HUMM and BOARD[2][2] != COMP:
            return [2, 2]
    if BOARD[2][2] == COMP and BOARD[1][2] == COMP:
        if BOARD[0][2] != HUMM and BOARD[0][2] != COMP:
            return [0, 2]


def capraz_kontrol():
    if BOARD[0][0] == HUMM and BOARD[1][1] == HUMM:
        if BOARD[2][2] != COMP and BOARD[2][2] != HUMM:
            return [2, 2]
    if BOARD[2][2] == HUMM and BOARD[1][1] == HUMM:
        if BOARD[0][0] != COMP and BOARD[0][0] != HUMM:
            return [0, 0]
    if BOARD[2][0] == HUMM and BOARD[1][1] == HUMM:
        if BOARD[0][2] != COMP and BOARD[0][2] != HUMM:
            return [0, 2]
    if BOARD[0][2] == HUMM and BOARD[1][1] == HUMM:
        if BOARD[2][0] != COMP and BOARD[2][0] != HUMM:
            return [2, 0]


def capraz_kontrol_comp():  # kazanan seçenek gözükmüyor kontrol edicem.
    if BOARD[0][0] == COMP and BOARD[1][1] == COMP:
        if BOARD[2][2] != HUMM and BOARD[2][2] != COMP:
            return [2, 2]
    if BOARD[2][2] == COMP and BOARD[1][1] == COMP:
        if BOARD[0][0] != HUMM and BOARD[0][0] != COMP:
            return [0, 0]
    if BOARD[2][0] == COMP and BOARD[1][1] == COMP:
        if BOARD[0][2] != HUMM and BOARD[0][2] != COMP:
            return [0, 2]
    if BOARD[0][2] == COMP and BOARD[1][1] == COMP:
        if BOARD[2][0] != HUMM and BOARD[2][0] != COMP:
            return [2, 0]


def ortasi_bos_kontrol():
    if BOARD[0][0] == HUMM and BOARD[0][2] == HUMM:
        if BOARD[0][1] != COMP and BOARD[0][1] != HUMM:
            return [0, 1]
    if BOARD[1][0] == HUMM and BOARD[1][2] == HUMM:
        if BOARD[1][1] != COMP and BOARD[1][1] != HUMM:
            return [1, 1]
    if BOARD[2][0] == HUMM and BOARD[2][2] == HUMM:
        if BOARD[2][1] != COMP and BOARD[2][1] != HUMM:
            return [2, 1]
    if BOARD[0][0] == HUMM and BOARD[2][0] == HUMM:
        if BOARD[1][0] != COMP and BOARD[1][0] != HUMM:
            return [1, 0]
    if BOARD[0][1] == HUMM and BOARD[2][1] == HUMM:
        if BOARD[1][1] != COMP and BOARD[1][1] != HUMM:
            return [1, 1]
    if BOARD[0][2] == HUMM and BOARD[2][2] == HUMM:
        if BOARD[1][2] != COMP and BOARD[1][2] != HUMM:
            return [1, 2]


def ortasi_bos_kontrol_comp():
    if BOARD[0][0] == COMP and BOARD[0][2] == COMP:
        if BOARD[0][1] != HUMM and BOARD[0][1] != COMP:
            return [0, 1]
    if BOARD[1][0] == COMP and BOARD[1][2] == COMP:
        if BOARD[1][1] != HUMM and BOARD[1][1] != COMP:
            return [1, 1]
    if BOARD[2][0] == COMP and BOARD[2][2] == COMP:
        if BOARD[2][1] != HUMM and BOARD[2][1] != COMP:
            return [2, 1]
    if BOARD[0][0] == COMP and BOARD[2][0] == COMP:
        if BOARD[1][0] != HUMM and BOARD[1][0] != COMP:
            return [1, 0]
    if BOARD[0][1] == COMP and BOARD[2][1] == COMP:
        if BOARD[1][1] != HUMM and BOARD[1][1] != COMP:
            return [1, 1]
    if BOARD[0][2] == COMP and BOARD[2][2] == COMP:
        if BOARD[1][2] != HUMM and BOARD[1][2] != COMP:
            return [1, 2]


def ortasi_bos_capraz_kontrol():
    if BOARD[0][0] == HUMM and BOARD[2][2] == HUMM:
        if BOARD[1][1] != COMP and BOARD[1][1] != HUMM:
            return [1, 1]
    if BOARD[0][2] == HUMM and BOARD[2][0] == HUMM:
        if BOARD[1][1] != COMP and BOARD[1][1] != HUMM:
            return [1, 1]


def ortasi_bos_capraz_kontrol_comp():
    if BOARD[0][0] == COMP and BOARD[2][2] == COMP:
        if BOARD[1][1] != HUMM and BOARD[1][1] != COMP:
            return [1, 1]
    if BOARD[0][2] == COMP and BOARD[2][0] == COMP:
        if BOARD[1][1] != HUMM and BOARD[1][1] != COMP:
            return [1, 1]


BOARD = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]


HUMM = "X"
COMP = "O"


if __name__ == "__main__":
    main()
