'''
Tech Interview Prep Group task - Session 3.
Next Permutation in Python
Time complexity: O()
'''
from itertools import permutations


n = 3
# arrInput = list(map(int, input("Enter the list numbers separated by space :").strip().split()))[:n]
# inputAsTuple = tuple(arrInput)
# resultID = -1
# result = []

# pList = list(permutations(range(1, n+1)))

# for (index, item) in enumerate(pList):
#     if (resultID == index):
#         print(item)
#     elif (resultID == len(pList)):
#         print(pList[0])

#     if (item == inputAsTuple):
#         resultID = index+1

'''This brute force solution takes O(n!*N) time'''

def nextPermutation(nums: list) -> list:
    x, y, z = nums[0], nums[1], nums[2]
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                if (i != j and j != k and k != i):
                    
                    if (x == 0 and y == 0 and z == 0):
                        nums[0], nums[1], nums[2] = i, j, k 
                        return nums
                    if ([i,j,k] == [x,y,z]):
                        x, y, z = 0, 0, 0
                    
    return sorted(nums)


print(nextPermutation([2,3,1]))
print(nextPermutation([3,2,1]))