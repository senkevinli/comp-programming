# 6 - 1 * 2 * 3 * 4 * 5 * 6
# 2 * 3 * 2 * 2 * 5 * 2 * 3
def sieve(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    return [i for i in range(2, n+1) if prime[i]]

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

def fastExp(base, exp):
    if exp == 1:
        return base
    ans = fastExp(base * base % MOD, exp // 2)
    if exp % 2 == 1:
        ans = ans * base % MOD
    return ans

def solve():
    # Implementation goes here.
    vals = []
    n = inp()
    while n != 0:
        vals.append(n)
        n = inp()
    primes = sieve(max(vals) // 2 + 1)
    for n in vals:
        answer = 1

        for p in primes:
            if p > n // 2 + 1: # (n ** .5) + 1:
                break
            temp = p
            count = 0
            while n // temp > 0:
                count += n // temp
                temp *= p
            count = (count - 1) if (count % 2 != 0) else count
            if count >= 1:
                answer = (answer * fastExp(p, count)) % MOD
        
        print(answer)

solve()
# print(len(sieve(10_000_000)))