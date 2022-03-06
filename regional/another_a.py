from itertools import combinations


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
    # Implementation goes here.
    cases = inp()
    
    probs = []
    for i in range(cases):
        probs.append(fl())
    
    memo = dd(int)
    for i in range(cases + 1):
        c = combinations(range(len(probs)), i)
        
        for possible in c:
            if i <= 2:
                memo.update({ possible: 0 })
            else:
                eval_prob(memo, probs, possible)
                
    print(memo[tuple(i for i in range(cases))])
    # from pprint import pprint
    # pprint(memo)        

def eval_prob(memo, probs, tup):
    d = {}
    prods = 1
    opp_prods = 1
    for j in tup:
        prods *= probs[j]
        opp_prods *= (1 - probs[j])
    
    for j in tup:
        d[j] = (prods / probs[j] * (1 - probs[j])) + (opp_prods / (1 - probs[j]) * probs[j])
    
    # print(d)
    tot = sum(d.values())
    # e = {j:d[j]/tot for j in d}
    # f = {j:1/d[j] for j in d}
    
    # print(e)
    # print(f)
    
    for i in range(len(tup)):
        sliced = tup[0:i] + tup[i + 1: len(tup)]
        expected_sliced = memo[sliced]
        j = tup[i]
        memo[tup] += d[j] * expected_sliced
    memo[tup] += 1
    memo[tup] *= 1 / tot    
            
        
    
    # print(memo)

    

solve()