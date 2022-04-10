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
    n = inp()
    a = seq()
    b = seq()
    
    dist = 0
    
    prev_a = a[0]
    prev_b = b[0]
    

    for i in range(1, len(a)):
        cur_a = a[i]
        cur_b = b[i]
        
        no_swap = abs(cur_a - prev_a) + abs(cur_b - prev_b)
        swapped = abs(cur_a - prev_b) + abs(cur_b - prev_a)
        
        if no_swap < swapped:
            dist += no_swap
            prev_a = cur_a
            prev_b = cur_b
        else:
            dist += swapped
            prev_a = cur_b
            prev_b = cur_a
    
    return dist


cases = inp()

for _ in range(cases):
    print(solve())