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
fl = lambda: float(input())


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
    vals = []
    for i in range(n):
        vals.append(inp())
    print(vals)
    print(dothing(vals))
    # d = {}
    # for i in range(len(vals)):
    #     for j in range(len(vals)):
    #         xxx = i ^ j
    #         if xxx in vals:
    #             print(i, j, xxx)
    ans = sys.maxsize
    for i in range(len(vals)):
        temp = vals[:i] + vals[i+1:]
        for j in range(len(temp)):
            temp2 = temp[:j] + temp[j+1:]
            ans = min(ans, dothing(temp2))
    print(ans)

def dothing(nums):
    nn = set(nums)
    count = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            xxx = i ^ j
            if xxx in nn:
                count += 1
    return count

solve()