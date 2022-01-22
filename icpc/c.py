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

# res = [0]
# for x in range(1, 250 + 1):
#     res.append(0)
#     for y in range(1, x + 1):
#         if math.gcd(x, y) > 1:
#             res[-1] += 1

# frac = [0] + [str(i) + ':' + format(res[i] / i, '.2f') for i in range(1, len(res)) if i != 0]

# print(res)
# print(frac)

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
n = inp()
prod = 1
phi = 1
for x in primes:
    if prod * x <= n:
        prod *= x
        phi *= (x - 1)
    else:
        break

numerator = prod - phi
denominator = prod

# print(numerator, denominator)
numer = numerator // math.gcd(numerator, denominator)
denom = denominator // math.gcd(numerator, denominator)



print(f'{numer}/{denom}')




# 2, 2 * 3, 2* 3 * 5, 2 * 3 * 5 * 7