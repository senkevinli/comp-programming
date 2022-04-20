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


factorials = [6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600, 6227020800, 87178291200, 1307674368000]

def count_ones(n):
    count = 0
    while n > 0:
        count += n & 1
        n >>= 1
    return count

def fact_sum(n):
    s = 0
    idx = 0
    c = 0
    while n > 0:
        
        if n & 1:
            s += factorials[idx]
            c += 1
        n >>= 1
        idx += 1
    return s, c

def solve():
    n = inp()
    
    mini = math.inf
    
    for i in range(0, 1 << (len(factorials) - 1)):
        summed, c = fact_sum(i)
        if summed > n:
            break
        mini = min(mini, c + count_ones(n - summed))
    
    return mini

cases = inp()
for _ in range(cases):
    print(solve())
