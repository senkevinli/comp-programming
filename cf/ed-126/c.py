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


def make_trees_equal(arr, target, ones, twos):
    
    for num in arr:
        if num == target:
            continue
        
        leftover = target - num
        
        twos_needed = leftover // 2
        twos_used  = min(twos, twos_needed)
        twos -= twos_used
        leftover = leftover - twos_used * 2
        
        if leftover == 0:
            continue
        
        if leftover > ones:
            return False
        
        ones -= leftover
    return True
    
def solve():
    elems = inp()
    arr = seq()
    
    biggest = max(arr)

    
    low = 0
    high = 2 * biggest * elems + 1
    
    while low <= high:
        middle = (low + high) // 2
        
        days = middle
        ones = (days - 1) // 2 + 1
        twos = days // 2
        if make_trees_equal(arr, biggest, ones, twos):
            high = middle - 1
        else:
            low = middle + 1
            
    
    low2 = 0
    high2 = 2 * biggest * elems + 1
    
    while low2 <= high2:
        middle = (low2 + high2) // 2
        
        days = middle
        ones = (days - 1) // 2 + 1
        twos = days // 2
        if make_trees_equal(arr, biggest + 1, ones, twos):
            high2 = middle - 1
        else:
            low2 = middle + 1
    
    return min(low, low2)
    

cases = inp()

for _ in range(cases):
    print(solve())