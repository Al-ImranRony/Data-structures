'''
Learning with Tecognize - HW of Lecture 1
Leetcode problem - 01
'''

nums = [int(num) for num in input("Enter numbers: ").split()]
target = int(input("Target: "))

for i in range(len(nums)):
    for j in range(len(nums)):
        if (nums[i]+nums[j]) == target:
            print([i, j])
            flag = 1
    if flag == 1: break

