import sys
import math
import bisect
from sys import stdin,stdout
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd
from bisect import bisect_left as bl,bisect_right as br

from itertools import chain, combinations

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


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

def bitmasks(n,m):
    if m < n:
        if m > 0:
            for x in bitmasks(n-1,m-1):
                yield (1 << (n-1)) + x
            for x in bitmasks(n-1,m):
                yield x
        else:
            yield 0
    else:
        yield (1 << n) - 1

def solve():
    cases = inp()
    
    probs = []
    for i in range(cases):
        probs.append(fl())
    dp = []
    num = sum(2 ** i for i in range(cases))
    
    twos = set(bitmasks(cases, 2))
    ones = set(bitmasks(cases, 1))
    

    for b in range(2 ** cases):
        if b == 0 or b in twos or b in ones:
            dp.append(0)
        else:
            dp.append(eval_prob(dp, probs, b))
 
    return dp[num]

def eval_prob(memo, probs, num):
    # Stores probability that the element (key) gets eliminated.

    # Prefix products.
    prods = 1
    opp_prods = 1

    idx = 1
    tmp_num = num
    while tmp_num > 0:
        digit = tmp_num & 1
        if digit == 1:
            prods *= probs[-idx]
            opp_prods *= (1 - probs[-idx])
        tmp_num = tmp_num >> 1
        idx += 1

    # Expectation [a, b, c, d, ...] = 1 + P(a eliminated) * E[b, c, d, ...] + P(b eliminated) * E[a, c, d, ...] + ... + P(no one eliminated) * E[a, b, c, d, ...]
    # Expectation [a, b, c, d, ...] * (1 - P(no one eliminated)) = 1 + P(a eliminated) * E[b, c, d, ...] + P(b eliminated) * E[a, c, d, ...] + ...
    # Expectation [a, b, c, d, ...] * P(someone gets eliminated) = 1 + P(a eliminated) * E[b, c, d, ...] + P(b eliminated) * E[a, c, d, ...] + ...
    # Expectation [a, b, c, d, ...] = (1/P(someone gets eliminated)) * (1 + P(a eliminated) * E[b, c, d, ...] + P(b eliminated) * E[a, c, d, ...] + ...)
    tmp_num = num
    factor = 1
    idx = 1
    ret = 0
    tot = 0
    while tmp_num > 0:
        digit = tmp_num & 1
        
        if digit == 1:
            expected_sliced = memo[num - factor]
            elim_prob = (prods / probs[-idx] * (1 - probs[-idx])) + (opp_prods / (1 - probs[-idx]) * probs[-idx])
            ret += elim_prob * expected_sliced
            tot += elim_prob
        idx += 1
        tmp_num = tmp_num >> 1
        factor = factor << 1
    
    ret += 1
    ret *= 1 / tot
    
    return ret

print(solve())