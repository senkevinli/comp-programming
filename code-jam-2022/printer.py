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
    printers = []
    
    for i in range(3):
        printers.append(seq())
    
    min_colors = []
    for j in range(len(printers[0])):
        mini = math.inf
        for i in range(len(printers)):
            mini = min(mini, printers[i][j])
        min_colors.append(mini)
    
    answer = []
    running = 0
    for color in min_colors:
        added = min(color, 1000000 - running)
        running += added
        answer.append(str(added))

    return 'IMPOSSIBLE' if running < 1000000 else ' '.join(answer)
        

cases = inp()

for i in range(cases):
    print(f'Case #{i+1}:', solve())