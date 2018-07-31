import numpy as np

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0)]

def selectRandomColor():
    return colors[np.random.random_integers(0, 5)]

class I():
    def __init__(self, board_width):
        self.board_width = board_width
        self.row = 5
        self.column = np.random.random_integers(3, self.board_width-3)
        self.state = 1
        self.color = selectRandomColor()

    def adjustPosition(self):
        if(self.leftBound() < 0):
            self.column -= self.leftBound()
        if(self.rightBound() > self.board_width):
            self.column -= self.rightBound() - self.board_width

    def getPositions(self):
        self.adjustPosition()

        if(self.state == 1):
            return [(self.row, self.column), (self.row, self.column+1), (self.row, self.column+2), (self.row, self.column+3)]
        elif(self.state == 2):
            return [(self.row, self.column), (self.row+1, self.column), (self.row+2, self.column), (self.row+3, self.column)]
        elif(self.state == 3):
            return [(self.row, self.column), (self.row, self.column-1), (self.row, self.column-2), (self.row, self.column-3)]
        else:
            return [(self.row, self.column), (self.row-1, self.column), (self.row-2, self.column), (self.row-3, self.column)]

    def rotate(self):
        if(self.state == 1):
            self.column += 2
            self.state += 1
        elif(self.state == 2):
            self.row += 2
            self.state += 1
        elif(self.state == 3):
            self.column -= 2
            self.state += 1
        else:
            self.row -= 2
            self.state = 1

    def shiftDown(self, board_state):
        self.row += 1
        positions = self.getPositions()
        #at bottom of board
        if(self.lowerBound() > board_state.shape[0]):
            self.row -= 1
            return True
        elif(board_state[(positions[0])[0]][(positions[0])[1]] == 1 or board_state[(positions[1])[0]][(positions[1])[1]] == 1 or
                board_state[(positions[2])[0]][(positions[0])[2]] == 1 or board_state[(positions[3])[0]][(positions[3])[1]] == 1):
            self.row -= 1
            return True
        else:
            return False

    def shiftLeft(self, board_state):
        self.column -= 1

    def shiftRight(self, board_state):
        self.column += 1

    def leftBound(self):
        if(self.state == 3):
            return self.column - 3
        else:
            return self.column

    def rightBound(self):
        if(self.state == 1):
            return self.column + 3
        else:
            return self.column

    def lowerBound(self):
        if(self.state == 2):
            return self.row + 3
        else:
            return self.row
