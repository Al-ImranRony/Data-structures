'''
Tech Interview Prep Group task - Session 2.
Pascal's Triangle in Python
'''


rows = input("Number of rows: ")
rows = int(rows)
pascalMatrix = [[1]*i for i in range(1, rows+1)]

for row in range(2, rows):
    for col in range(1, row):       
        pascalMatrix[row][col] = pascalMatrix[row-1][col-1] + pascalMatrix[row-1][col]

# Show
for row in range(rows):
    for col in range(row + 1):
        print(pascalMatrix[row][col], end=" ")
    print("\n")