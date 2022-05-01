import sys
import math
import bisect
from sys import stdin,stdout
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd
from bisect import bisect_left as bl,bisect_right as br

# faster input
# LINES = sys.stdin.read().splitlines()[::-1]
# def input(): return LINES.pop()

# single integer
inp = lambda: int(input())

# string input
strng = lambda: input().strip()

# words split on white space
strwords = lambda: strng().split()


# string list
strl = lambda: list(input().strip())

# multiple integers, mapped
mul = lambda: map(int,input().strip().split())

# multiple floats, mapped
mulf = lambda: map(float,input().strip().split())

# list of multiple integers
seq = lambda: list(map(int,input().strip().split()))

ceil = lambda x: int(x) if(x==int(x)) else int(x)+1
ceildiv = lambda x,d: x//d if(x%d==0) else x//d+1

MOD = 1000000007

mod_add = lambda x, y: ((x % MOD) + (y % MOD)) % MOD
mod_multiply = lambda x, y: ((x % MOD) * (y % MOD)) % MOD
mod_division = lambda x, y: mod_multiply(x, math.pow(y, MOD - 2, MOD))

in_bounds = lambda x, y, grid: x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])

def prefix_sum(arr):
    for i in range(1, len(arr)):
        arr[i] += arr[i-1]
    return arr

def calc_subarrays(start, i, end):
    return (end - start) * (i - start + 1) - (i - start + 1) * (i - start)

def prefix_suffix(arr):
    
    prefix = []
    
    best = arr[0]
    
    for num in arr:
        best = max(best, num)
        prefix.append(best)
    
    suffix = [0 for _ in range(len(arr))]
    
    best = arr[-1]
    
    for i in range(len(arr)-1, -1, -1):
        best = max(best, arr[i])
        suffix[i] = best
    
    return prefix, suffix

def nge(nums, dir):
    mapping = {}
    stack = []
    
    stack.append(nums[0])
    
    if dir == 1:
        for i in range(1, len(nums)):
            while stack and nums[i] > stack[-1]:
                mapping[stack[-1]] = nums[i]
                stack.pop()
            stack.append(nums[i])
    else:
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[i] > stack[-1]:
                mapping[stack[-1]] = nums[i]
                stack.pop()
            stack.append(nums[i])
    
    for element in stack:
        mapping[element] = -1
    return mapping

def solve():
    n = inp()
    
    arr = seq()
    
    d = { num: i for i, num in enumerate(arr) }
    
    right_bound = nge(arr, 1)
    left_bound = nge(arr, 0)

    ret = []
    for num in arr:
        right = right_bound[num] 
        left = left_bound[num]
        
        if right != -1:
            right = d[right]
        else:
            right = n
        
        if left != -1:
            left = d[left] + 1
        else:
            left = 0
        
        ret.append(calc_subarrays(left, d[num], right))
    
    return ' '.join(map(str, ret))
            
        
        
    
    print(right_bound)
    print(left_bound)

    return 0

print(solve())

