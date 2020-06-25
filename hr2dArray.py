import math
import os
import random
import sys

arr = []
for i in range(6):
    arr.append(list(map(int, input().strip().split())))

sum, max = 0, -100
for i in range(1, 5):
    for j in range(1, 5):
        sum = arr[i][j]+ arr[i+1][j+1]+ arr[i-1][j-1]+ arr[i+1][j-1]+ arr[i-1][j+1]+ arr[i+1][j]+ arr[i-1][j] 
        if sum > max:
            max = sum
print(max)