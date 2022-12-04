'''
Tech Interview Prep Group task - Session 1.
Set Matrix Zero in Python
'''


givenMatrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
row = len(givenMatrix)
colum = len(givenMatrix[0])
mi, mj, roz, coz = [-1]*row, [-1]*colum, [-1]*row, [-1]*colum
 
for i in range(row):
    for j in range(colum):
        if (givenMatrix[i][j] == 0):
            mi[i], mj[j] = i, j
            roz[i], coz[j] = 0, 0

'''This brute force solution needs O(m*n + m*n*k) time and O(n) extra space.'''
# for i in range(row):
#     for j in range(colum):
#         for k in range(colum):
#             if (i == mi[k] or j == mj[k]):
#                 givenMatrix[i][j] = 0

'''Time complexity reduced to: O(m*n + m*n) with O(n) extra space.'''
for i in range(row):
    for j in range(colum):
        if (givenMatrix[i][j] != 0 and (roz[i] == 0 or coz[j] == 0)):
            givenMatrix[i][j] = 0


# Show
for i in range(row):
    for j in range(colum):
        print("|", givenMatrix[i][j], end=" |")
    print("\n")         