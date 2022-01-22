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

def possible(stamps):
    prefix = [0] * (len(stamps)  + 1)
    
    running = 0
    i = 1
    for num in stamps:
        running += num
        prefix[i] = running
        i += 1
        
    
    
    suffix = [0] * len(stamps)
    i = len(stamps) - 1
    running = 0
    for num in stamps[::-1]:
        running += num
        suffix[i] = running
        i -= 1
    
    suffix += [0]
    
    return prefix, suffix

    # tgt = 16
    # [17, 15, 7, 6, 3, 0] # suffix
    #      ^
    # [0, 2, 10, 11, 14, 17] # prefix
    #              ^

def solve(stamps, suffix, prefix):
    # Implementation goes here.
    query = inp()
    
    current = 0

    suf_p = 0
    pre_p = 0
    
    if query > suffix[0]:
        print('No')
        return
    
    while True:
        
        if pre_p > suf_p or pre_p >= len(prefix) or suf_p >= len(suffix):
            print('No')
            return
        
        current = suffix[suf_p] + prefix[pre_p]
        
        if current == query:
            print('Yes')
            return
        
        if current < query:
            pre_p += 1
        elif current > query:
            suf_p += 1
        

a, b = mul()
stamps = seq()


prefix, suffix = possible(stamps)
for i in range(b):
    solve(stamps, suffix, prefix)