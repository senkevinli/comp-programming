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


def determine_moves(zero_spot, arr):
    prev = 0
    total = 0
    for i in range(zero_spot + 1, len(arr)):
        moves = prev // arr[i] + 1
        total += moves
        
        prev = arr[i] * moves
    
    prev = 0
    for i in range(zero_spot - 1, -1, -1):
        moves = prev // arr[i] + 1
        total += moves
        
        prev = arr[i] * moves
    
    return total

def solve():
    n = inp()
    arr = seq()
    
    mini = math.inf
    for i in range(n):
        mini = min(mini, determine_moves(i, arr))
        #print(i, mini)
    
    return mini

print(solve())      

