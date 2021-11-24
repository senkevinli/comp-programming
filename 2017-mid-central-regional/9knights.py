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
    grid = []
    knights = set()
    for i in range(5):
        row = strl()

        for j, elem in enumerate(row):
            if elem == 'k':
                knights.add((i, j))
        
        grid.append(row)

    movement = [
        (2, 1),
        (2, -1),
        (-2, 1),
        (-2, -1),
        (1, 2),
        (1, -2),
        (-1, 2),
        (-1, -2)
    ]

    if len(knights) != 9:
        return False
    for knight in knights:
        x, y = knight
        for move in movement:
            x_1 = x + move[0]
            y_1 = y + move[1]

            if not in_bounds(x_1, y_1, grid):
                continue

            if (x_1, y_1) in knights:
                return False

    return True


result = solve()
if result:
    print('valid')
else:
    print('invalid')