import sys
import math
import bisect
from sys import stdin,stdout
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd
from bisect import bisect_left as bl,bisect_right as br

import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

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

# modified kadane's
def max_product(nums):
    if not nums:
        return 0
    
    prev_max = None
    prev_min = None
    
    global_max = None
    
    for i in range(len(nums)):
        if i == 0:
            prev_max = (nums[i], (i, i + 1))
            prev_min = (nums[i], (i, i + 1))
            global_max = (nums[i], (i, i + 1))
            continue
        
        off_pos = (prev_max[0] * nums[i], (prev_max[1][0], i + 1))
        off_neg = (prev_min[0] * nums[i], (prev_min[1][0], i + 1))
        cur = (nums[i], (i, i + 1))

        cases = list(sorted([off_pos, off_neg, cur], key=lambda x: x[0], reverse=True))
        
        maxi = cases[0]
        mini = cases[2]
        
        prev_max = maxi
        prev_min = mini
        
        if prev_max[0] > global_max[0]:
            global_max = prev_max
    
    return global_max
        
def solve():
    n = inp()
    nums = seq()
    max_prod, max_index = max_product(nums)
    
    if max_prod <= 0:
        return n, 0
    
    left, right = max_index
    
    return left, len(nums) - right

cases = inp()

for _ in range(cases):
    print(*solve())