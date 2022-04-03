import sys
import math
import bisect
from sys import stdin,stdout
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd
from bisect import bisect_left as bl,bisect_right as br

# faster input

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
    rooms, guesses = mul()
    sum = 0
    visited = set()
    
    start, adj = mul()
    
    while True:
        print('W')
        
        visited.add(start)
        
        guesses -= 1
        next_start, next_adj = mul()

        if adj < next_adj:
            sum += 2 * adj
        
        if guesses == 0:
            break
            
        visited.add(start)

        start = next_start
        adj = next_adj
        
        visited.add(start)

        for room in range(1, rooms + 1):
            if room not in visited:
                print('T', room)
                guesses -= 1
                break
        start, adj = mul()

        if guesses == 0:
            sum += adj
            break
        
    print('E', sum)

cases = inp()

for _ in range(cases):
    solve()