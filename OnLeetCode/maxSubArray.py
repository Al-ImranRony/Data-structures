'''
Tech Interview Prep Group task - Session 3.
Maximum SubArray in Python Uising kadane's Algo
Time complexity: O(N)
'''

import sys

def maxSubArray(nums: list) -> int:
    ln = len(nums)
    # sas = 0
    # sat = l
    # res = []
    sum = 0
    maxSubSum = -sys.maxsize - 1

    if ln<2:
        return ln

    for i in range(ln):
        sum += nums[i]
    
        if (sum > maxSubSum):
            # print(nums[i], "dhukche", j)
            # sas, sat = i, j
            maxSubSum = sum

        if sum < 0 :
            sum = 0

    # for sae in range(sas, sat+1):
    #     res.append(nums[sae])
    # print(res)
    return maxSubSum


print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([2, -3, 4, 1, 1]))

