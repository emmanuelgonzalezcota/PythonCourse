row = []

WHITE_PAWN = "♙"

# for i in range(8):
#     row.append(WHITE_PAWN)
# Next Instruction resumes last cycle
row = [WHITE_PAWN for i in range(8)]

print(row)

# Square list
squares = [x ** 2 for x in range(10)]
print(squares)

# powers of 2s list
twos = [2 ** i for i in range(8)]
print(twos)

# odd and even from squares list
odd  = [x for x in squares if x % 2 != 0]
even = [x for x in squares if x % 2 == 0]
print(odd)
print(even)