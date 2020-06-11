"""
playTest.py
"""

from minemaxAI import selectmove
import chess.pgn
import datetime
from IPython.display import SVG

"""
aiPlay()
Causes the initial minemax AI to play itself
Used to test inital state before editing
"""
def aiPlay():
    print("Starting Game:")
    movehistory =[]
    game = chess.pgn.Game()
    game.headers["Event"] = "Example"
    game.headers["Site"] = "Linz"
    game.headers["Date"] = str(datetime.datetime.now().date())
    game.headers["Round"] = 1
    game.headers["White"] = "MyChess"
    game.headers["Black"] = "MyChess"
    board = chess.Board()
    while not board.is_game_over(claim_draw=True):
        if board.turn:
            move = selectmove(board, movehistory, 1)
            board.push(move)       
        else:
            move = selectmove(board, movehistory, 1)
            board.push(move)   
        
    game.add_line(movehistory)
    game.headers["Result"] = str(board.result(claim_draw=True))
    print(game)
    print(game, file=open("selftest.pgn", "w"), end="\n\n")
    SVG(chess.svg.board(board=board,size=400))