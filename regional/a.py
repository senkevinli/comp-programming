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

def solve():
    cases = inp()
    
    probs = []
    for i in range(cases):
        probs.append(fl())
    
    memo = dd(int)
    full_tuple = tuple(i for i in range(cases))
    
    # Generates all possible subsets (2^20 worst case).
    all_sets = powerset(full_tuple)
    
    for s in all_sets:
        if len(s) <= 2:
            memo.update({s : 0})
        else:
            eval_prob(memo, probs, s)
                
    return memo[full_tuple]

def eval_prob(memo, probs, tup):
    
    # Stores probability that the element (key) gets eliminated.
    d = {}

    # Prefix products.
    prods = 1
    opp_prods = 1
    for j in tup:
        prods *= probs[j]
        opp_prods *= (1 - probs[j])

    # Sum two cases (black + white elimination).
    for j in tup:
        d[j] = (prods / probs[j] * (1 - probs[j])) + (opp_prods / (1 - probs[j]) * probs[j])

    tot = sum(d.values())
    
    # Expectation [a, b, c, d, ...] = 1 + P(a eliminated) * E[b, c, d, ...] + P(b eliminated) * E[a, c, d, ...] + ... + P(no one eliminated) * E[a, b, c, d, ...]
    # Expectation [a, b, c, d, ...] * (1 - P(no one eliminated)) = 1 + P(a eliminated) * E[b, c, d, ...] + P(b eliminated) * E[a, c, d, ...] + ...
    # Expectation [a, b, c, d, ...] * P(someone gets eliminated) = 1 + P(a eliminated) * E[b, c, d, ...] + P(b eliminated) * E[a, c, d, ...] + ...
    # Expectation [a, b, c, d, ...] = (1/P(someone gets eliminated)) * (1 + P(a eliminated) * E[b, c, d, ...] + P(b eliminated) * E[a, c, d, ...] + ...)
    for i in range(len(tup)):
        # Exclued the current element.
        sliced = tup[0:i] + tup[i + 1: len(tup)]
        
        # Get expectation of left over.
        expected_sliced = memo[sliced]
        j = tup[i]
        memo[tup] += d[j] * expected_sliced

    memo[tup] += 1
    memo[tup] *= 1 / tot


print(solve())