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
    def __init__(self, value, abyss=False):
        self.val = value
        self.adj = []
        self.back = []
        self.is_abyss = abyss
        self.max_at = -math.inf
    
    def set_max_at(self, val):
        self.max_at = val

    def add_connection(self, node):
        self.adj.append(node)
    
    def add_connection_back(self, node):
        self.back.append(node)

    def str_adj(self):
        adj = ','.join([str(x) for x in self.adj])
        return f'Adjacent: [ {adj} ]'

    def str_back(self):
        back = ','.join([str(x) for x in self.back])
        return f'Adjacent: [ {back} ]'

    def is_leaf(self):
        return len(self.back) == 0

    def __str__(self):
        return f'(Node: {self.val}, Min: {self.min_at})'

def print_it(s):
    print(', '.join([str(x) for x in s]))

def solve():
    # Implementation goes here.
    nodes = inp()
    
    mapping = {}
    
    fun = seq()
    points = seq()

    for i, p in enumerate(fun):
        mapping.update({i + 1: Node(p)})
    mapping.update({0: Node(0, True)})
    
    for i, p in enumerate(points):
        key = i + 1
        mapping[key].add_connection(mapping[p])
        mapping[p].add_connection_back(mapping[key])

    leaves = [ node for node in mapping.values() if node.is_leaf() ]
    
    global acc
    acc = 0
    def helper(node):
        global acc
        if node.is_leaf():
            node.set_max_at(node.val)
            return
        
        for back in node.back:
            helper(back)
        
        summed = sum(back.max_at for back in node.back)
        mini = min(back.max_at for back in node.back)
        
        if node.is_abyss:
            acc += summed
        else:
            acc += summed - mini
            node.set_max_at(max(mini, node.val))
    
    helper(mapping[0])
    return acc
                
        

cases = inp()

for i in range(cases):
    print(f'Case #{i+1}: {solve()}')