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
    a = strl()
    b = strl()

    diff_start = None
    diff_end = None

    for i in range(len(a)):
        a1 = a[i]
        b1 = b[i]

        if a1 != b1:
            diff_start = i
            break
    
    for i in range(len(a) - 1, -1, -1):
        a1 = a[i]
        b1 = b[i]

        if a1 != b1:
            diff_end = i
            break
    
    sub = a[diff_start:diff_end + 1]
    sub = sub[::-1]
    sub_b = b[diff_start:diff_end + 1]
    
    if sub != sub_b:
        return 0

    count = 1
    diff_start -= 1
    diff_end += 1
    while diff_start >= 0 and diff_end < len(a):

        head = a[diff_start]
        tail = a[diff_end]
        if head == tail:
            count += 1
        else:
            break
        diff_start -= 1
        diff_end += 1
    return count

result = solve()
print(result)