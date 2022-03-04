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
    for _ in range(n):
        vals = seq()
        d = vals.pop(-1)
        c = vals.pop(-1)
        a = [vals[i] for i in range(0, len(vals), 2)]
        b = [vals[i] for i in range(1, len(vals), 2)]
        vals = seq()
        x = [vals[i] for i in range(0, len(vals), 2)]
        y = [vals[i] for i in range(1, len(vals), 2)]
        dp = [[0 for _ in range(100)] for __ in range(100)]
        for i in range(100):
            dp[i][0] = d
            dp[0][i] = d
        for i in range(1, 100):
            for j in range(1, 100):
                dp[i][j] = c
                for t in range(len(a)):
                    xp = max(0, i - a[t])
                    yp = max(0, j - b[t])
                    dp[i][j] += dp[xp][yp]
        for t in range(len(x)):
            print(dp[x[t]][y[t]])
        print()
    
    
solve()