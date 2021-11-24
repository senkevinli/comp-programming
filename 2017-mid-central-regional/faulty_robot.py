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

class Node:
    def __init__(self, val):
        self.val = val
        self.adj = []
        self.forced = []
    
    def add_elem(self, elem):
        self.adj.append(elem)
    
    def add_forced(self, elem):
        self.forced.append(elem)

def cycle_detection(start):
    visited = set()

    stack = [start]

    while stack:
        cur = stack.pop()

        if cur in visited:
            return visited, True
        
        visited.add(cur)
            
        for neighbor in cur.forced:
            stack.append(neighbor)

    return visited, False

def dfs(src):

    stack = [src]
    visited = set()

    final = None
    while stack:
        cur = stack.pop()
        if cur in visited:
            return None
        final = cur
        visited.add(cur)
        for neighbor in cur.forced:
            stack.append(neighbor)
            final = neighbor
    return final

def modified_dfs(src):

    stack = [src]
    visited = set()
    stuff = set()

    final = None
    while stack:
        cur = stack.pop()
        if cur in visited:
            return len(stuff)
        visited.add(cur)
        extrapolate(cur, visited, stuff)
        for neighbor in cur.forced:
            stack.append(neighbor)
            final = neighbor
    
    stuff.add(final)
    return len(stuff)
        
        
def extrapolate(src, chain, stuff):
    neighbors = [node for node in src.adj if node not in chain]

    for neighbor in neighbors:
        result = dfs(neighbor)
        if result:
            stuff.add(result)


def solve():
    # Implementation goes here.
    n, m = mul()
    mapping = {}
    for i in range(1, n + 1):
        mapping.update({ i : Node(i) })

    for i in range(m):
        a, b = mul()

        src = mapping[abs(a)]
        dst = mapping[b]

        if a < 0:
            src.add_forced(dst)
        else:
            src.add_elem(dst)
    
    result = modified_dfs(mapping[1])
    return result

    
    



print(solve())
