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

global parent
global size
global people

def initialize(n):
    global parent
    global size
    global people
    parent = [i for i in range(n)] # parent labels
    size = [1 for _ in range(n)]   # size (i.e. number of cars)
    people = [-1 for _ in range(n)] # number of people in car


def find(child):
    if parent[child] == child :
        return child

    parent[child] = find(parent[child])
    return parent[child]

def getPeople(child):
    return people[find(child)]

def union(childA, childB) :
    rootA = find(childA)
    rootB = find(childB)

    if (rootA == rootB):
        # Already same component, no need to merge
        return

    if (size[rootA] > size[rootB]):
        # Swap
        rootA, rootB = rootB, rootA

    # We have that size[rootA] <= size[rootB], so it is best to merge rootA into
    # rootB
    size[rootB] += size[rootA]
    parent[rootA] = rootB
    people[rootB] += people[rootA]

def round_up(x): 
    if x % 10 > 0:
        x += 10 - (x % 10)
    return x

def solve():
    global parent
    global size
    global people
    
    # Implementation goes here.
    carts = inp()
    initialize(carts)
    
    counts = seq()
    blow_up = seq()
    
    segs = 0
    chaos = 0
    max_chaos = -1
    for b in blow_up[::-1]:
        to_add = b - 1

        to_add_count = counts[b - 1]
        segs += 1
        temp_chaos = round_up(to_add_count)
        chaos += temp_chaos
        
        before = b - 2
        after = b
        
        # print(to_add)
        people[to_add] = counts[to_add]


        if before >= 0 and people[before] >= 0:
            segs -= 1
            left_people = getPeople(before)
            chaos -= round_up(left_people)
            right_people = getPeople(to_add)
            chaos -= round_up(right_people)

            union(to_add, before)
            comb_people = getPeople(to_add)
            chaos += round_up(comb_people)
            
        if after < carts and people[after] >= 0:
            segs -= 1

            left_people = getPeople(to_add)
            chaos -= round_up(left_people)
            right_people = getPeople(after)
            chaos -= round_up(right_people)

            union(to_add, after)
            comb_people = getPeople(to_add)
            chaos += round_up(comb_people)

        
        max_chaos = max(max_chaos, segs * chaos)
        
    print(max_chaos)
solve()

'''
30 * 1
(10 + 20) * 2
(10 + 10 + 10) * 3
'''