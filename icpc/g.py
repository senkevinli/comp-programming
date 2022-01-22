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

# def solve():
#     # Implementation goes here.
#     pass

def runLengths(lst):    
    a = [1]
    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:
            a[-1] += 1
        else:
            a.append(1)
    return a

c, n = mul()
errors = seq()

code = [False] * c
for x in errors:
    code[x - 1] = True

err = (errors[0] == 1)
lengths = runLengths(code)

wrong = []
correct = []


pos = 1
for x in lengths:
    if err:
        wrong.append(str(pos) if x == 1 else f'{pos}-{pos + x - 1}')
    else:
        correct.append(str(pos) if x == 1 else f'{pos}-{pos + x - 1}')
    pos += x
    err = not err
if len(wrong) == 1:
    print(f'Errors: {wrong[0]}')
else:
    print(f'Errors: {", ".join(wrong[:-1])} and {wrong[-1]}')
if len(correct) == 1:
    print(f'Correct: {correct[0]}')
else:
    print(f'Correct: {", ".join(correct[:-1])} and {correct[-1]}')


# print(lengths)
    