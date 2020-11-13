# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 17:21:57 2020

@author: nzubair
"""

#https://stackoverflow.com/questions/56754543/generate-chess-board-diagram-from-an-array-of-positions-in-python

import io

def board_to_fen(board):
    # Use StringIO to build string more efficiently than concatenating
    with io.StringIO() as s:
        for row in board:
            empty = 0
            for cell in row:
                c = cell[0]
                if c in ('w', 'b'):
                    if empty > 0:
                        s.write(str(empty))
                        empty = 0
                    s.write(cell[1].upper() if c == 'w' else cell[1].lower())
                else:
                    empty += 1
            if empty > 0:
                s.write(str(empty))
            s.write('/')
        # Move one position back to overwrite last '/'
        s.seek(s.tell() - 1)
        # If you do not have the additional information choose what to put
        s.write(' w KQkq - 0 1')
        return s.getvalue()
    
board = [
    ['bk', 'em', 'em', 'em', 'em', 'em', 'em', 'em'],
    ['em', 'bn', 'em', 'wr', 'em', 'wp', 'em', 'em'],
    ['br', 'em', 'bp', 'em', 'em', 'bn', 'wn', 'em'],
    ['em', 'em', 'bp', 'bp', 'bp', 'em', 'wp', 'bp'],
    ['bp', 'bp', 'em', 'bp', 'wn', 'em', 'wp', 'em'],
    ['em', 'em', 'em', 'em', 'em', 'em', 'em', 'em'],
    ['em', 'em', 'em', 'wk', 'em', 'em', 'em', 'em'],
    ['em', 'em', 'em', 'em', 'em', 'em', 'em', 'em'],
]
print(board_to_fen(board))

#Then analyse in https://www.chess.com/analysis