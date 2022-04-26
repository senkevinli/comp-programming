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
    ret = arr[:]
    for i in range(1, len(arr)):
        ret[i] += ret[i-1]
    return ret

def solve():
    n = inp()
    arr = seq()

    bound_r = n
    bound_l = 0

    right = n - 1
    left = 0
    
    best = 0

    right_sum = 0
    left_sum = 0
    elems = 0
    
    prefix = prefix_sum(arr)
    suffix = prefix_sum(arr[::-1])[::-1]

    
    while left < right:
        if prefix[left] == suffix[right]:
            best = max(best, n - right + left + 1)
            left += 1
            right -= 1
            continue
        
        if prefix[left] < suffix[right]:
            left += 1
        else:
            right -= 1
    
    return best

cases = inp()
for _ in range(cases):
    print(solve())