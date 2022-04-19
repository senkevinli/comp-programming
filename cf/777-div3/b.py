import sys
import math
import bisect
from sys import stdin,stdout
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd, deque
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
    rows, cols = mul()
    
    grid = []
    for _ in range(rows):
        grid.append(strl())
    
    visited = set()
    
    def get_dims(i, j, grid):
        row = i
        dim_x = 0
        while row < rows and grid[row][j] == '1':
            row += 1
            dim_x += 1
        
        col = j
        dim_y = 0
        while col < cols and grid[i][col] == '1':
            col += 1
            dim_y += 1
        
        return dim_x, dim_y

    def get_neighbors(i, j, grid):
        dirs = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]
        
        for d in dirs:
            cur_i = i + d[0]
            cur_j = j + d[1]
            
            if in_bounds(cur_i, cur_j, grid) and grid[cur_i][cur_j] == '1':
                yield cur_i, cur_j
        
    def bfs(i, j, grid):
        queue = deque([(i, j)])
        visited = set()
        while queue:
            cur = queue.popleft()
            if cur in visited:
                continue
            visited.add(cur)
            
            for n in get_neighbors(*cur, grid):
                queue.append(n)
        
        return visited
            
    all_zeroes = True
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '0':
                continue
            if (i, j) in visited:
                continue
            all_zeroes = False
            dim_x, dim_y = get_dims(i, j, grid)
            cur_visited = bfs(i, j, grid)
            for x, y in cur_visited:
                correct_range = x >= i and x < i + dim_x and y >= j and y < j + dim_y
                if not correct_range:
                    return False
            
            if len(cur_visited) != dim_x * dim_y:
                return False
            visited |= cur_visited
    
    if all_zeroes:
        return True
    return True
            

cases = inp()

for _ in range(cases):
    print('YES ' if solve() else 'NO')