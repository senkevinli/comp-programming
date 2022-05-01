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

def hamming_distance(a, b):
    return sum(x != y for x, y in zip(a, b))

def num_transforms(src, dest):
    
    if len(src) == len(dest):
        return hamming_distance(src, dest)
    
    midpoint = len(dest) // 2
    
    first_half = dest[:midpoint]
    second_half = dest[midpoint:]
    
    count = 0
    for a, b, c in zip(src, first_half, second_half):
        if a == b and a == c:
            continue
        
        if b != c:
            if a == b or a == c:
                count += 1
            else:
                count += 2
        else:
            count += 1
    
    return count + 1

def solve():
    n = inp()
    
    if n == 1:
        return 0

    source = strl()
    
    total = 0
    for i in range(n - 1):
        dest = strl()
        
        total += num_transforms(source, dest)
        source = dest
    return total
    
    

print(solve())