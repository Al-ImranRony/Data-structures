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

def nextPermutation(nums: list) -> None:
    # x, y, z = nums[0], nums[1], nums[2]
    # for i in range(1, n+1):
    #     for j in range(1, n+1):
    #         for k in range(1, n+1):
    #             if (i != j and j != k and k != i):
                    
    #                 if (x == 0 and y == 0 and z == 0):
    #                     nums[0], nums[1], nums[2] = i, j, k 
    #                     return nums
    #                 if ([i,j,k] == [x,y,z]):
    #                     x, y, z = 0, 0, 0
                    
    # return sorted(nums)

    '''The "Next Permutation Algo" applied with 4 steps'''
#1
    k = len(nums) - 1
    while k and nums[k-1] >= nums[k]: 
        k-=1
#2
#    l = k+1
#3
    if k:
        low, high = k, len(nums)
        while low < high :
            mid = (low+high)//2
            if nums[mid] <= nums[k-1]:
                high = mid
            else :
                low = mid + 1

        nums[k-1], nums[low-1] = nums[low-1], nums[k-1]
#4
    low, high = k, len(nums)-1
    while low < high: 
        nums[low], nums[high] = nums[high], nums[low]
        low, high = low+1, high-1  

    return nums

print(nextPermutation([1, 2, 3]))
print(nextPermutation([3,2,1]))