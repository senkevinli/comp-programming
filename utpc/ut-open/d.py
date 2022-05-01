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


def solve():
    n, m, k = mul()
    
    grid = []
    
    for i in range(n):
        grid.append(seq())
        
    row_begin = 0
    col_begin = 0
    row_end = len(grid)-1 
    col_end = len(grid[0])-1
    grapes = 0
    counter = 0
    while (row_begin <= row_end and col_begin <= col_end):
        for i in range(col_begin,col_end+1):
            
            if counter % k == 0:
                grapes += grid[row_begin][i]
            counter += 1
        row_begin += 1
        for i in range(row_begin,row_end+1):
            if counter % k == 0:
                grapes += grid[i][col_end]
            counter += 1
        col_end -= 1
        if (row_begin <= row_end):
            for i in range(col_end,col_begin-1,-1):
                if counter % k == 0:
                    grapes += grid[row_end][i]
                counter += 1
            row_end -= 1
        if (col_begin <= col_end):
            for i in range(row_end,row_begin-1,-1):
                if counter % k == 0:
                    grapes += grid[i][col_begin]
                counter += 1
            col_begin += 1
    return grapes
print(solve())