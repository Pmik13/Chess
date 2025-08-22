from Figure import Figure

class Queen(Figure):
    def __init__(self, position, color):
        super().__init__(position, color)

    def move(self, new_position):
        self.position = new_position

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
        if(abs(a - x) == abs(b - y)):
            for i in range(min(a, x)+1, max(a, x)):
                k = i - min(a, x)
                z = i - min(a, x)
                if(x > a and b < y):
                    if not (board[min(y, b)+k][i] == " "):
                        return False
                elif(a > x and b > y):
                    if not (board[min(y, b) + k][i] == " "):
                        return False
                elif(a > x and y > b ):
                    if not (board[max(y, b) - k][i] == " "):
                        return False
                else:
                    if not (board[max(y, b) - k][i] == " "):
                        return False
            return True
        if not ((x == a) or (y == b)):
            return False
        else :
            if(y == b):
                if(abs(x - a) == 1):
                    return True
                else:
                    for i in range(min(x, a) + 1, max(x, a)):
                        if not (board[y][i] == " "):
                            return False
            else:
                if(abs(y - b) == 1):
                    return True
                else:
                    for i in range(min(y, b) + 1, max(y, b)):
                        if not (board[i][x] == " "):
                            return False
            return True
    def __str__(self):
        return 'Q'
