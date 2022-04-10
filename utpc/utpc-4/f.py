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
    n, k = mul()
    
    arr = seq()
    
    i = n - 1
    
    while i > 0:
        if arr[i] != -1:
            val = arr[i]
            for j in range(arr[i]):
                i -= 1
                val -= 1
                arr[i] = val 
            
            assert val == 0
        i -= 1
    
    i = 0
    while i < len(arr):
        if arr[i] != -1 and arr[i] != 0:
            val = arr[i]
            
            while i + 1 < len(arr) and val < k:
                i += 1
                val += 1
                arr[i] = val
            
            if i >= len(arr):
                break
            
            arr[i] = 0
        i += 1
    
    print(arr)
    # zeroes = 0
    # while i < len(arr):
    #     prev = arr[i]
        
    #     while i < len(arr) and arr[i] != -1:
    #         prev = arr[i]
    #         zeroes += 1 if arr[i] == 0 else 0
    #         i += 1
        
    #     if i == len(arr):
    #         return zeroes
    
    #     neg_ones = 0
        
    #     while i < len(arr) and arr[i] == -1:
    #         neg_ones += 1
    #         i += 1
        
    #     sub = neg_ones
    #     if prev != 0:
    #         sub = neg_ones - max(1, k + 1 - prev)
    #         if sub > 0:
    #             zeroes += 1
        
    #     if sub <= 0:
    #         continue
        
    #     zeroes += (sub) // (k + 1)
        

print(solve())