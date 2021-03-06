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
fl = lambda: float(input())


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

from itertools import combinations
def solve():
    # Implementation goes here.
    nums = inp()
    
    islanders = []    
    for _ in range(nums):
        islanders.append(inp())
    
    
    pairs = list(combinations(range(nums), 2))
    
    smallest = sys.maxsize
    for p in pairs:
        excluded = [i for i in range(nums) if i not in p]
        
        aaa = []
        triplets = list(combinations(excluded, 3))
        count = 0
        for t in triplets:
            i1 = t[0]
            i2 = t[1]
            i3 = t[2]
            
            if islanders[i1] ^ islanders[i2] == islanders[i3]:
                aaa.append((islanders[i1], islanders[i2], islanders[i3]))
                count += 1
        
        if count == 3:
            print(p)
            print(aaa)
        smallest = min(smallest, count)
        # print(triplets)
    print(smallest)

solve()
