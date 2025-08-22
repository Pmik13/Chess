YELLOW = '\033[93m'
RESET = '\033[0m'
GREEN = '\033[92m'
from Pawn import Pawn
from Rook import Rook
from Knight import Knight
from King import King
from Bishop import Bishop
from Queen import Queen
import copy

class Board(Pawn, Rook, Knight, King, Bishop, Queen):
    def __init__(self):
        self.board = [[" " for x in range(0, 8)] for y in range(0, 8)]
        self.ruch = 1
        self.kolor = "white"
        self.lastmove= ""
    def check(self):
        polei = 0
        polej = 0
        if(self.ruch%2 == 1):
            self.kolor = "white"
        else:
            self.kolor = "black"
        for i in range(0, 8):
            for j in range(0, 8):
                if not(self.board[i][j] == " "):
                    if((self.board[i][j].__str__() == 'K') and (self.board[i][j].kolor != self.kolor)):
                        polei = i
                        polej = j
        for i in range(0, 8):
            for j in range(0, 8):
                if not(self.board[i][j] == " "):
                    if(self.board[i][j].kolor != self.board[polei][polej].kolor):
                        if(self.board[i][j].check_move((polej+1)* 10+polei+1, self.board)):
                            return True
        return False
    def check_mate(self, szachownica):
        self.ruch += 1
        if(self.ruch%2 == 1):
            self.kolor = "white"
        else:
            self.kolor = "black"
        for i in range(0, 8):
            for j in range(0, 8):
                if not (self.board[i][j] == " "):
                    if (self.board[i][j].kolor == self.kolor):
                        for x in range(0, 8):
                            for y in range(0, 8):
                                if (self.move( (j+1)*10 + i + 1,(y+1) * 10 + x +1)):
                                    if not (self.check()):
                                        self.ruch -= 1
                                        self.board = copy.deepcopy(szachownica)
                                        return False
                                    self.board = copy.deepcopy(szachownica)
                                    self.ruch -= 1
        return True

    def view_board(self):
        for i in range(0, 8):
            print(YELLOW + str(8-i) + RESET, end = ' ')
            for j in range(0, 8):
                x = self.board[7-i][j]
                if(x == " "):
                    print(x, end=' ')
                elif(x.kolor == "black"):
                    print(GREEN + x.__str__() + RESET, end=' ')
                else:
                    print(x, end=' ')
            print()
        print(YELLOW + "  a b c d e f g h" + RESET)
    def add_figure(self, figura, pole):
        x = pole // 10 - 1
        y = pole % 10 - 1
        self.board[y][x] = figura
    def promote (self, pole, nazwa):
        x = pole // 10 - 1
        y = pole % 10 - 1
        if (self.board[y][x].__str__() == 'P' and (y == 7 or y == 1)):
            if(nazwa == 'Q'):
                self.board[y][x] = Queen(pole, self.board[y][x].kolor)
            elif(nazwa == 'R'):
                self.board[y][x] = Rook(pole, self.board[y][x].kolor)
            elif(nazwa == 'B'):
                self.board[y][x] = Bishop(pole, self.board[y][x].kolor)
            elif(nazwa == 'N'):
                self.board[y][x] = Knight(pole, self.board[y][x].kolor)
            return True
        else:
            return False
    def castle(self, castle, szachownica):
        y = 0
        if(castle == "o-o-o"):
            y = -7
        x = 0
        if(self.ruch%2 == 1):
            self.kolor = "white"
        else:
            self.kolor = "black"
            x += 7
        if (self.board[x][4] == " "):
            return False
        if not (self.board[x][4].__str__() == 'K'):
            return False
        if(self.board[x][4].moved > 0):
            return False
        if(self.board[x][7+ y] == " "):
            return False
        if not (self.board[x][7+y].__str__() == 'R'):
             return False
        if(self.board[x][7+y].moved > 0 or (self.board[x][7+y].kolor != self.kolor)):
            return False
        if(y == 0):
            if(self.move(81 + x, 61 + x)):
                self.board[x][7] = self.board[x][5]
                self.board[x][5] = " "
                if(self.check()):
                    self.ruch += 1
                    return False
                self.board[x][5] = self.board[x][4]
                self.board[x][4] = " "
                if(self.check()):
                    self.board[x][4] = self.board[x][5]
                    self.board[x][5] = " "
                    self.ruch += 1
                    return False
                self.board[x][6] = self.board[x][5]
                self.board[x][5] = " "
                self.board[x][5] = self.board[x][7]
                self.board[x][7] = " "
            else:
                return False
        else:
            if(self.move(11 + x, 41 + x )):
                self.board[x][0] = self.board[x][3]
                self.board[x][3] = " "
                if(self.check()):
                    self.ruch += 1
                    return False
                self.board[x][3] = self.board[x][4]
                self.board[x][4] = " "
                if(self.check()):
                    self.board[x][4] = self.board[x][3]
                    self.board[x][3] = " "
                    self.ruch += 1
                    return False
                self.board[x][2] = self.board[x][3]
                self.board[x][3] = " "
                if(self.check()):
                    self.board[x][4] = self.board[x][2]
                    self.board[x][2] = " "
                    self.ruch += 1
                    return False
                self.board[x][3] = self.board[x][0]
                self.board[x][0] = " "
            else:
                return False
        return True


    def move(self, old_pole, new_pole):
        x = old_pole // 10 - 1
        y = old_pole % 10 - 1
        if(self.board[y][x] == " "):
            return False
        if(self.ruch%2 == 1):
            self.kolor = "white"
        else:
            self.kolor = "black"
        if(self.board[y][x].kolor != self.kolor):
            return False
        if(self.board[y][x].check_move(new_pole, self.board) and self.board[y][x].capture(new_pole, self.board)):
            figura = self.board[y][x]
            self.board[y][x] = " "
            x = new_pole // 10 - 1
            y = new_pole % 10 - 1
            figura.move(new_pole)
            self.board[y][x] = figura
            self.ruch += 1
            self.lastmove = str(old_pole) + str(new_pole)
            return True
        else:
            if(self.board[y][x].__str__() == "P" and self.lastmove != ""):
                if(self.board[y][x].enpassant(old_pole, new_pole, self.board, self.lastmove)):
                    figura = self.board[y][x]
                    self.board[y][x] = " "
                    x = new_pole // 10 - 1
                    y = new_pole % 10 - 1
                    figura.move(new_pole)
                    self.board[y][x] = figura
                    self.ruch += 1
                    return True
            return False
