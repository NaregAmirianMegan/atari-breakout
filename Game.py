import numpy as np
import random

from Pieces import I

class Game():
    def __init__(self, width, height):
        self.game_state = np.zeros((height, width))
        self.curr_piece = self.genPiece()
        self.curr_score = 0
        self.pieces = [I(width)]

    def genPiece(self):
        return random.sample(self.pieces, 1)[0]

    def elimRow(self, row):
        if(row == 0):
            self.game_state[row] = np.zeros((1, 10))
        else:
            self.game_state[row] = self.game_state[row-1]
            self.elimRow(row-1)

    def shift(self):
        result = self.curr_piece.shiftDown(self.game_state)
        if(result):
            #if this piece is expired switch to new active piece
            self.curr_piece = self.genPiece()

    def updatePieceLocation(self):


    def update(self, keyPressed=None, frameNum):
        if(keyPressed == "LEFT"):
            self.curr_piece.shiftLeft(self.game_state)
        elif(keyPressed == "RIGHT"):
            self.curr_piece.shiftRight(self.game_state)
        elif(keyPressed == "UP"):
            self.curr_piece.rotate()

        if(frameNum % 100 == 0):
            self.shift()
            self.updateScoreBoard()

        self.updatePieceLocation()

    def updateScoreBoard(self):
        sumArr = np.sum(self.game_state, axis=1)
        for x in range(len(sumArr)):
            if(sumArr[x] == 10):
                self.curr_score += 10
                self.elimRow(x)
