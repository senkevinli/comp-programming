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
    n, k = seq()
    
    if k == 1:
        return 0
    
    grid = []
    
    for _ in range(n):
        grid.append(seq())
    
    mapping = dd(list)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            mapping[grid[i][j]].append((i, j))
            
    dp = [[0] * len(grid[0]) for _ in range(len(grid))]
    
    
    distance = lambda x, y: min((x[0] - y[0]) ** 2, (x[1] - y[1]) ** 2)
    
    for number in range(2, k + 1):
        if number not in mapping:
            return -1
        for coord in mapping[number]:
            temp = sys.maxsize
            for prev_coord in mapping[number - 1]:
                temp = min(temp, distance(coord, prev_coord) + dp[prev_coord[0]][prev_coord[1]])
            dp[coord[0]][coord[1]] = temp
    
    temp = sys.maxsize
    for coord in mapping[k]:
        temp = min(dp[coord[0]][coord[1]], temp)
    
    return temp

print(solve())