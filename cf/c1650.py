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
    n, m = mul()
    
    coords = []
    
    for i in range(m):
        x, weight = mul()
        coords.append((weight, x, i + 1))
    
    coords.sort()
    coords = coords[0:n * 2]
    
    total = 0
    for c in coords:
        total += c[0]
        
    print(total)
    
    coords.sort(key=lambda x: x[1])
    
    for i in range(n):
        begin = coords[i]
        end = coords[-(i + 1)]
        print(f'{begin[2]} {end[2]}')
    
    print()

cases = inp()

for _ in range(cases):
    strng()
    solve()