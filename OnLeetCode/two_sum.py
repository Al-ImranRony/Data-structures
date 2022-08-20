'''
Learning with Tecognize - HW of Lecture 1
Leetcode problem - 01
'''

from tokenize import String

def twoSum(nums, target) -> String:
        start, end = 0, len(nums)-1
        result = ''
        
        for i in range(end-1):
            for j in range(end):
                if(nums[i] + nums[j] == target):
                    result = ('[' + str(i) + ',' + str(j) + ']')
                    return result

print(twoSum([2,7,11,15], 9))