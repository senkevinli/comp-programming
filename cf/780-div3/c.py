import sys
import math
import bisect
from sys import stdin,stdout
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd
from bisect import bisect_left as bl,bisect_right as br

# faster input
LINES = sys.stdin.read().splitlines()[::-1]
def input(): return LINES.pop()

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

def maxProduct(self, nums):
    # check the edge case of an empty array
    if not nums:
        return 0
    # since the array can contain negative/positive integers
    # at each iteration, the max product could be obtained by 
    # multiplying to a previous max or by multiplying prev min
    # (since even number of -ve integers will be a +ve product)
    # or by using the number itself
    
    i = 0
    max_index = 0
    local_min = local_max = global_max = nums[0]

    for n in nums[1:]:
        i += 1
        temp = local_max # retain the previous local minimum

        # compute new local max (using nums[i] with
        # local max or local min or stand alone)
        local_max = max(n, n*local_max, n*local_min)

        # update local min
        local_min = min(n, n*local_min, n*temp)
        
        if local_max > global_max:
            global_max = local_max
            max_index = i

    return global_max, max_index

def solve():
    sequence = strl()
    
    prevs = set()
    cost = 0
    for ch in sequence:
        if ch in prevs:
            cost += len(prevs) - 1
            prevs = set()
        else:
            prevs.add(ch)
    
    return cost + len(prevs)

cases = inp()

for _ in range(cases):
    print(solve())