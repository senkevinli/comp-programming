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

def solve():
    # Implementation goes here.
    n, k = mul()
    
    arr = seq()
    
    cached = all_sums(arr)
    
    dp_end = kadanes(arr)
    dp_begin = kadanes(arr[::-1])[::-1]
    
    dp_begin.pop(-1)
    dp_end.pop(0)
    
    prev = -sys.maxsize
    
    ret = [max(0, max(dp_end))]
    for window in range(n):
        best = prev
        for i in range(0, n - window):
            grouped = cached[i][i + window] + (window + 1) * (k)
            before = 0
            if i - 1 >= 0:
                before = max(before, dp_end[i - 1])
            
            after = 0
            if i + 1 + window < n:
                after = max(after, dp_begin[i + 1 + window])
                
            # print('sums')
            # print(i, before, after)
            
            # print(grouped, i, i + window, before, after)
            best = max(grouped + before + after, best)
            best = max(best, 0)
        prev = max(best, prev)
        ret.append(best)
    
    return ret

def all_sums(arr):
    dp = [[0] * len(arr) for _ in range(len(arr))]
    for i in range(len(arr)):
        cur = 0
        for j in range(i, len(arr)):
            cur += arr[j]
            dp[i][j] = cur
    
    return dp


def kadanes(arr):
    
    dp = [0]
    
    for a in arr:
        dp.append(max(a, a + dp[-1]))
    
    return dp

cases = inp()

for _ in range(cases):
    ret = solve()
    
    for a in ret:
        print(a, end=' ')
    print()