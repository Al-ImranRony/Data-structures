'''
Tech Interview Prep Group task - Session 1.
'''


givenMatrix = [[1,1,0], [1,1,1], [0,1,1]]
ln = (len(givenMatrix))
mi, mj, lenz = [-1]*ln, [-1]*ln, 0
 
for i in range(ln):
    for j in range(ln):
        if (givenMatrix[i][j] == 0):
            mi[i], mj[j] = i, j
            # lenz += 1


for i in range(ln):
    for j in range(ln):
        for k in range(ln):
            if (i == mi[k] or j == mj[k]):
                givenMatrix[i][j] = 0

'''This brute force solution needs O(2m*n + k) time and O(n) extra space.'''
for i in range(ln):
    for j in range(ln):
        print("|", givenMatrix[i][j], end=" |")
    print("\n")         