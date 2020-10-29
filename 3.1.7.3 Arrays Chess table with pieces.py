EMPTY   = "-"
WKING   = "♔"
WQUEEN  = "♕"
WROOK   = "♖"
WBISHOP = "♗"
WKNIGHT = "♘"
WPAWN   = "♙"
BKING   = "♚"
BQUEEN  = "♛"
BROOK   = "♜"
BBISHOP = "♝"
BKNIGHT = "♞"
BPAWN   = "♟"

board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

board[0][0] = BROOK
board[0][7] = BROOK
board[7][0] = WROOK
board[7][7] = WROOK

board[4][2] = WKNIGHT
board[3][4] = BPAWN

for i in board:
    print(i)