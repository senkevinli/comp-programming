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
    n, m = mul()
    
    grid = []
    for i in range(n):
        grid.append(strl())
    
    dest = None
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'O':
                dest = (i, j)
                break
    R = (0, 1)
    L = (0, -1)
    U = (-1, 0)
    D = (1, 0)
    
    directions = [
        R,
        L,
        U,
        D
    ]
    
    
    
    forward_slash = {
        R: U,
        L: D,
        U: R,
        D: L
    }
    
    backward_slash = {
        R: D,
        L: U,
        U: L,
        D: R
    }

    cur_dir = None
    for d in directions:
        t_x = dest[0] + d[0]
        t_y = dest[1] + d[1]
        
        if in_bounds(t_x, t_y, grid) and grid[t_x][t_y] != '#':
            cur_dir = d
            break
    if cur_dir is None:
        return grid
    
    coord = dest
    while True:
        new_x = coord[0] + cur_dir[0]
        new_y = coord[1] + cur_dir[1]
        
        if not in_bounds(new_x, new_y, grid) or grid[new_x][new_y] == '#':
            break
        
        if grid[new_x][new_y] == '.':
            grid[new_x][new_y] = '@'
        elif grid[new_x][new_y] == '\\':
            cur_dir = backward_slash[cur_dir]
        elif grid[new_x][new_y] == '/':
            cur_dir = forward_slash[cur_dir]
            
        coord = (new_x, new_y)
    return grid
    
ret = solve()


for row in ret:
    print(''.join(row))