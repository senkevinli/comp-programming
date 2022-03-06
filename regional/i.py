import sys
import math
import bisect
from sys import stdin,stdout
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd
from bisect import bisect_left as bl,bisect_right as br

from copy import deepcopy

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

def most_for_round(arr, k, low, high):
    ret = 0
    # n = high - low
    mid = (high + low) // 2
    # n = len(arr) // 2
    
    largest = len(arr) - 1
    smallest = mid
    
    for i in range(low, mid):
        if arr[smallest] - arr[i] <= k:
            smallest += 1
            ret += 1
    return ret

def solve():
    n, k = seq()
    
    arr = []
    for i in range(2 ** n):
        arr.append(inp())
    
    arr.sort()
    
    answer = 0
    low = 0
    high = len(arr)
    while high - low >= 2:
        temp = deepcopy(arr)
        answer += most_for_round(temp, k, low, high)
        
        mid = (high + low ) // 2
        low =  mid
    
    print(answer)

solve()

'''
def most_for_round(arr, k, low, high):
    ret = 0
    # n = high - low
    mid = (high + low) // 2
    # n = len(arr) // 2
    
    largest = len(arr) - 1
    smallest = mid
    
    for i in range(low, mid):
        for j in range(mid, high):
            if arr[j] != -1:
                if arr[j] - arr[i] <= k:
                    arr[j] = -1
                    ret += 1
                else:
                    arr[largest] = -1
                    largest -= 1
                break
    return ret

'''