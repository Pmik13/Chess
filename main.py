from Board import Board
from Pawn import Pawn
from Rook import Rook
from Knight import Knight
from King import King
from Bishop import Bishop
from Queen import Queen
import copy

libczy = [1, 2, 3, 4, 5, 6, 7, 8]
litery = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
Figury = ['P', 'R', 'N', 'B', 'Q', 'K']
wartosci = [10, 20, 30, 40, 50, 60, 70, 80]

class chess(Board, Pawn, Rook, Knight, King, Bishop, Queen):
    def __init__(self):
        self.__main__()
    def parse(self, input):
        wynik = 0
        for i in range(len(litery)):
            if (litery[i] == input[0]):
                wynik += wartosci[i]
        wynik += int(input[1])
        return int(wynik)

    def inicialize(self, plansza):
        for i in range(0, 8):
            pawn_white = Pawn((i+1)*10 + 2, "white")
            pawn_black = Pawn((i+1)*10 + 7, "black")
            plansza.add_figure(pawn_white, (i+1)*10 + 2)
            plansza.add_figure(pawn_black, (i+1)*10 + 7)
        wieza = Rook(11, "white")
        wieza2 = Rook(81, "white")
        skoczek2 = Knight(71, "white")
        plansza.add_figure(skoczek2, 71)
        plansza.add_figure(wieza, 11)
        plansza.add_figure(wieza2, 81)
        skoczek = Knight(21, "white")
        plansza.add_figure(skoczek, 21)
        krol = King(51, "white")
        plansza.add_figure(krol, 51)
        goniec = Bishop(61, "white")
        plansza.add_figure(goniec, 61)
        goniec2 = Bishop(31, "white")
        plansza.add_figure(goniec2, 31)
        krolowa = Queen(41, "white")
        plansza.add_figure(krolowa, 41)
        wieza3 = Rook(18, "black")
        wieza4 = Rook(88, "black")
        skoczek3 = Knight(78, "black")
        plansza.add_figure(skoczek3, 78)
        plansza.add_figure(wieza3, 18)
        plansza.add_figure(wieza4, 88)
        skoczek4 = Knight(28, "black")
        plansza.add_figure(skoczek4, 28)
        krol2 = King(58, "black")
        plansza.add_figure(krol2, 58)
        goniec3 = Bishop(68, "black")
        plansza.add_figure(goniec3, 68)
        goniec4 = Bishop(38, "black")
        plansza.add_figure(goniec4, 38)
        krolowa2 = Queen(48, "black")
        plansza.add_figure(krolowa2, 48)
        return True

    def check_correct(self, x):
        napis = ""
        if(len(x) == 4):
            for i in litery:
                if(x[0] == i):
                    napis+= i
            for i in libczy:
                if(x[1] == str(i)):
                    napis+= str(i)
            for i in litery:
                if(x[2] == i):
                    napis+= i
            for i in libczy:
                if(x[3] == str(i)):
                    napis+= str(i)
            if(napis ==  x):
                return 1
        if(len(x) == 5):
            for i in Figury:
                if(x[0] == i):
                    napis+= i
            for i in litery:
                if(x[1] == i):
                    napis+= i
            for i in libczy:
                if(x[2] == str(i)):
                    napis+= str(i)
            for i in litery:
                if(x[3] == i):
                    napis+= i
            for i in libczy:
                if(x[4] == str(i)):
                    napis+= str(i)

            if(napis == x):
                return 2
        if(len(x) == 6):
            for i in litery:
                if(x[0] == i):
                    napis+= i
            for i in libczy:
                if(x[1] == str(i)):
                    napis+= str(i)
            for i in litery:
                if(x[2] == i):
                    napis+= i
            for i in libczy:
                if(x[3] == str(i)):
                    napis+= str(i)
            if(x[4] == '='):
                napis += '='
            for i in Figury:
                if(x[5] == i):
                    napis+= i
            if(napis ==  x):
                return 3
        return 0

    def __main__(self):
        ruch = 1
        checked = 0
        plansza = Board()
        szachownica = copy.deepcopy(plansza.board)
        self.inicialize(plansza)
        plansza.view_board()
        while(True):
            szachownica = copy.deepcopy(plansza.board)
            plansza.ruch += 1
            if(plansza.check()):
                if (plansza.check_mate(szachownica)):
                    if(ruch%2 == 0):
                        print("White Wins!!!")
                        return 0
                    else:
                        print("Black Wins!!!")
                        return 0
                else:
                    print("szach")
                    plansza.ruch -= 1
            plansza.ruch -= 1
            x = input()
            if(x == "show"):
                plansza.view_board()
                continue
            if(x == "stop"):
                return True
            checked = self.check_correct(x)
            if(checked == 0):
                print("Wrong move")
                continue
            elif(checked == 1):
                old_pole = x[0] + x[1]
                new_pole = x[2] + x[3]
                old_pole = self.parse(old_pole)
                new_pole = self.parse(new_pole)
            elif(checked == 2):
                old_pole = x[1] + x[2]
                new_pole = x[3] + x[4]
                old_pole = self.parse(old_pole)
                new_pole = self.parse(new_pole)
            elif(checked == 3):
                old_pole = x[0] + x[1]
                new_pole = x[2] + x[3]
                old_pole = self.parse(old_pole)
                new_pole = self.parse(new_pole)
                nazwa = x[5]
            else:
                if not (x == "o-o" or x == "o-o-o"):
                    print("Wrong Move")
            if(x == "o-o" or x == "o-o-o"):
                if(plansza.castle(x, szachownica)):
                    ruch += 1
                else:
                    print("U cant castle")
            elif(plansza.move(old_pole, new_pole) and self.check_correct(x)):
                if(checked == 3):
                    plansza.promote(new_pole, nazwa)
                ruch += 1
            else:
                print("Wrong Move")
            if(plansza.check()):
                if (plansza.check_mate(szachownica)):
                    if(ruch%2 == 1):
                        print("White Wins!!!")
                        return 0
                    else:
                        print("Black Wins!!!")
                        return 0
                else:
                    plansza.board = copy.deepcopy(szachownica)
                    ruch -= 1
                    print("Wrong Move! Check")
            plansza.view_board()
Gra = chess()


