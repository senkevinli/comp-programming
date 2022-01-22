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


# 5
# 5 1  // 1
# 6  // +

# 3
# 3 3 // d
# 6 // +

dp = [0] * 1_200_000
dp[1] = 1
for i in range(2, len(dp)):
    dp[i] = 2 + dp[i - 1]
    if i % 2 == 0:
        dp[i] = min(dp[i], 2 + dp[i//2])

# + ops to make i is (dp[i]) // 2
# print(dp[1:10])
# print(max(dp))

n = inp()
vals = seq()
vals = vals[::-1]
newVals = []
plusOps = 0

for x in vals:
    newVal = x + plusOps
    newVals.append(x + plusOps)
    plusOps += dp[newVal] // 2

newVals = newVals[::-1]
# print(newVals)

def makeIt(x):
    recipe = ''
    while x > 1:
        if x % 2 != 0 or dp[x - 1] <= dp[x // 2]:
            recipe = '1+' + recipe
            x = x - 1
        else:
            recipe = 'd+' + recipe
            x = x // 2
    return '1' + recipe

for x in newVals:
    print(makeIt(x), end='')
print()