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

def determine_valid(arr, operations):
    
    prev_ops = 0
    cur = 0
    
    for num in arr:
        if num + cur >= operations:
            cur = (num + cur) % operations
            prev_ops += 1
        else:
            cur += num
    
    prev_ops += 1 if cur > 0 else 0
    return prev_ops <= len(arr) - 1
    

def solve():
    n = inp()
    
    arr = seq()

    
    lo = max(arr)
    hi = 2 * max(arr)
    
    answer = math.inf
    while lo <= hi:
        mid = (lo + hi) // 2
        if determine_valid(arr, mid):
            answer = min(answer, mid)
            hi = mid - 1
        else:
            lo = mid + 1
    return answer

print(solve())