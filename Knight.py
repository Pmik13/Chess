from Figure import Figure

class Knight(Figure):
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
        if((abs(a - x) == 1) and (abs(b - y) == 2)):
            return True
        elif ((abs(a - x) == 2) and (abs(b - y) == 1)):
            return True
        else:
            return False
    def __str__(self):
        return 'N'
