board = []
EMPTY = "□"

# for i in range(8):
#     row = [EMPTY for i in range(8)]
#     board.append(row)

# Next Line abbreviates last Cycle
board = [[EMPTY for i in range(8)] for j in range(8)]

for i in board:
    print(i)