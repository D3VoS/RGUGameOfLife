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
        newBoard = []
        liveNeighbours = 0

        for i in range(len(self.height)):
            newBoard[i] = []
            for j in range(len(self.width)):
                starx = -1
                starty = -1
                endx = 2
                endy = 2
                if i==0: starty = 0
                if j == 0: startx = 0
                if i==(len(self.height) - 1): endy = 1
                if j==(len(self.height) - 1): endx = 1
                liveNeighbours = 0
                






if __name__ == "__main__":
    main()