from Figure import Figure

class Bishop(Figure):
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
        return False
    def __str__(self):
        return 'B'
