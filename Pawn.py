from Figure import Figure

class Pawn(Figure):
    def __init__(self, position, color):
        super().__init__(position, color)

    def move(self, new_position):
        self.position = new_position

    def enpassant(self,old_pole, new_pole, board, lastmove):
        old_old_pole = int(lastmove[0] + lastmove[1])
        a = old_old_pole//10 - 1
        b = old_old_pole % 10 - 1
        old_new_pole = int(lastmove[2] + lastmove[3])
        x = old_new_pole//10 - 1
        y = old_new_pole % 10 - 1
        if not (a == x):
            return False
        if (b == 6 and y == 4):
            board[y+1][x] = board[y][x]
            board[y][x] = " "
            if(board[old_pole% 10 - 1][old_pole // 10 - 1].check_move(new_pole, board)):
                return True
            board[y][x] = board[y+1][x]
            board[y+1][x] = " "
        if (b == 1 and y == 3):
            board[y-1][x] = board[y][x]
            board[y][x] = " "
            if(board[old_pole% 10 - 1][old_pole // 10 - 1].check_move(new_pole, board)):
                return True
            board[y][x] = board[y-1][x]
            board[y-1][x] = " "
        return False

    def capture(self, new_pole, board):
        x = new_pole // 10 - 1
        y = new_pole % 10 - 1
        if(board[y][x] == " "):
            return True
        elif(board[y][x].kolor != self.kolor):
            return True
        else:
            return False
    def check_move(self, new_pole, board):
        x = new_pole // 10 - 1
        y = new_pole % 10 - 1
        a = self.position // 10 - 1
        b = self.position % 10 - 1
        if(self.kolor == "white"):
            if((b + 1 == y) and (x == a) and (board[b+1][x] == " ")):
                return True
            if((x == a) and (b == 1) and (b+2 == y)):
                if(board[b+1][x] == " "):
                    return True
                else:
                    return False
            if((abs(x - a) == 1) and (y == b + 1)):
                if(self.capture(new_pole, board) and board[y][x] != " " ):
                    return True
            return False
        else:
            if((b - 1 == y) and (x == a) and (board[b-1][x] == " ")):
                return True
            if((x == a) and (b == 6) and (b-2 == y)):
                if (board[b-1][x] == " "):
                    return True
                else:
                    return False
            if((abs(x - a) == 1) and (y == b - 1)):
                if(self.capture(new_pole, board) and board[y][x] != " "):
                    return True
            return False
    def __str__(self):
        return 'P'
