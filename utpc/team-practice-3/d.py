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
    n, w, h = seq()
    
    dp = [[0] * (n + 1) for _ in range(w)]
    
    for i in range(len(dp[0])):
        dp[0][i] = min(i + 1, h + 1)
        
    for j in range(len(dp)):
        dp[j][0] = 1

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            bound = min(j, h)
            cumulative = 0
            for x in range(0, bound + 1):
                cumulative = mod_add(cumulative, dp[i - 1][j - x])

            dp[i][j] = cumulative

    subtract = min(n // w, h) + 1
    print((dp[w - 1][n] - subtract) % MOD)
            
    
solve()
