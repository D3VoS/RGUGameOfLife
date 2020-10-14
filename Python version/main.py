import random
def main():
    #TODO FUNCS:
    #PrintBoard
    #UpdateBoard
    #CreateBoard
    board = Board(5,5)
    board.CreateBoard()
    board.PrintBoard()

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = None
    
    def CreateBoard(self):
        board = []
        for i in range(self.width):
            board.append([])
            for j in range(self.height):
                board[i].append(random.randint(0,1))
        self.board = board
    
    def PrintBoard(self):
        if self.board is None:
            print('Create a board first')
        else:
            for i in self.board:
                print(i)
    
    def UpdateBoard(self):
        for i in self.board:
            







if __name__ == "__main__":
    main()