import sys
import math
import bisect
from sys import stdin,stdout
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd
from bisect import bisect_left as bl,bisect_right as br
from turtle import left

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




def solve():
    n = inp()
    arr = strl()
    
    cur = 0
    best = 0
    
    ee = []
    
    for c in arr:
        if c == 'R':
            cur += 1
        elif c == 'C':
            cur -= 1
        elif c == 'S':
            cur -= 2

        ee.append(max(best, cur))
        best = max(best, cur)
    
    dum = [0 for _ in range(n)]
    cur = 0
    best = 0
    
    for i in reversed(range(n)):
        c = arr[i]
        if c == 'R':
            cur -= 1
        elif c == 'C':
            cur += 1
        elif c == 'S':
            cur -= 2
        dum[i] = max(cur, best)
        best = max(cur, best)
    
    ret = -math.inf
    for t1, t2 in zip(dum, ee):
        ret = max(t1 + t2, ret)
    return ret
        
    
            
    

print(solve())