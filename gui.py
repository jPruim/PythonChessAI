"""
GUI.py
Adds a new graphical interface for the chess. Ideally this will allow a player to play against the opponent.
based on https://stackoverflow.com/questions/4954395/create-board-game-like-grid-in-python
"""

import tkinter as tk 
class ChessBoard(tk.Frame):
    def __init__(self, parent, size=36, lightcolor = "white",darkcolor = "green"):
        # size is the width of a square in pixels
        self.rows = 8
        self.columns = 8
        self.lightcolor = lightcolor
        self.darkcolor = darkcolor
        self.pieces = {}
        self.size = size

        canvas_width = self.columns * size
        canvas_height = self.rows * size
        
        tk.Frame.__init__(self,parent)
        self.canvas = tk.Canvas(self, borderwidth=0,highlightthickness=0, width=canvas_width, height=canvas_height, background="bisque")
        self.canvas.pack(side="top",fill="both", expand = True, padx=3, pady=3)

        self.canvas.bind("<Configure>", self.refresh)

    def addpiece(self, name, image, row=0,column=0):
        self.canvas.create_image(0,0, image=image, tags=(name, "piece"), anchor="c")
        self.placepiece(name, row, column)
    
    def placepiece(self, name, row, column):
        self.pieces[name]=(row,column)
        x0 = (column * self.size ) + int(self.size / 2)
        y0 = (row * self.size + int(self.size/2))
        self.canvas.coords(name,x0,y0)

    def refresh(self, event):
        xsize = int((event.width-1)/self.columns)
        ysize = int((event.height-1)/self.rows)
        self.size = min(xsize,ysize)
        self.canvas.delete("square")
        color = self.darkcolor
        for row in range(self.rows):
            color = self.lightcolor if color == self.darkcolor else self.darkcolor
            for col in range(self.columns):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
                color = self.lightcolor if color == self.darkcolor else self.darkcolor
        for name in self.pieces:
            self.placepiece(name, self.pieces[name][0], self.pieces[name][1])
        self.canvas.tag_raise("piece")
        self.canvas.tag_lower("square")

imagedata = '''
    R0lGODlhEAAQAOeSAKx7Fqx8F61/G62CILCJKriIHM+HALKNMNCIANKKANOMALuRK7WOVLWPV9eR
    ANiSANuXAN2ZAN6aAN+bAOCcAOKeANCjKOShANKnK+imAOyrAN6qSNaxPfCwAOKyJOKyJvKyANW0
    R/S1APW2APW3APa4APe5APm7APm8APq8AO28Ke29LO2/LO2/L+7BM+7BNO6+Re7CMu7BOe7DNPHA
    P+/FOO/FO+jGS+/FQO/GO/DHPOjBdfDIPPDJQPDISPDKQPDKRPDIUPHLQ/HLRerMV/HMR/LNSOvH
    fvLOS/rNP/LPTvLOVe/LdfPRUfPRU/PSU/LPaPPTVPPUVfTUVvLPe/LScPTWWfTXW/TXXPTXX/XY
    Xu/SkvXZYPfVdfXaY/TYcfXaZPXaZvbWfvTYe/XbbvHWl/bdaPbeavvadffea/bebvffbfbdfPvb
    e/fgb/Pam/fgcvfgePTbnfbcl/bfivfjdvfjePbemfjelPXeoPjkePbfmvffnvbfofjlgffjkvfh
    nvjio/nnhvfjovjmlvzlmvrmpvrrmfzpp/zqq/vqr/zssvvvp/vvqfvvuPvvuvvwvfzzwP//////
    ////////////////////////////////////////////////////////////////////////////
    ////////////////////////////////////////////////////////////////////////////
    ////////////////////////////////////////////////////////////////////////////
    ////////////////////////////////////////////////////////////////////////////
    ////////////////////////////////////////////////////////////////////////////
    /////////////////////////////////////////////////////yH+FUNyZWF0ZWQgd2l0aCBU
    aGUgR0lNUAAh+QQBCgD/ACwAAAAAEAAQAAAIzAD/CRxIsKDBfydMlBhxcGAKNIkgPTLUpcPBJIUa
    +VEThswfPDQKokB0yE4aMFiiOPnCJ8PAE20Y6VnTQMsUBkWAjKFyQaCJRYLcmOFipYmRHzV89Kkg
    kESkOme8XHmCREiOGC/2TBAowhGcAyGkKBnCwwKAFnciCAShKA4RAhyK9MAQwIMMOQ8EdhBDKMuN
    BQMEFPigAsoRBQM1BGLjRIiOGSxWBCmToCCMOXSW2HCBo8qWDQcvMMkzCNCbHQga/qMgAYIDBQZU
    yxYYEAA7
'''



if __name__ == "__main__":
    root = tk.Tk()
    board = ChessBoard(root)
    board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    player1 = tk.PhotoImage(data=imagedata)
    board.addpiece("player1", player1, 0,0)
    root.mainloop()
