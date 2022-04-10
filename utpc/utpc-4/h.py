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

from collections import deque
class Node:
    def __init__(self, val):
        self.val = val
        self.edges = []
    
    def add_edge(self, n):
        self.edges.append(n)

class DagNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.children = set()
        self.count = 0
        
    def add_prev(self, p):
        self.prev = p
    
    def add_child(self, child):
        self.children.add(child)
    
    def __str__(self):
        return str(self.val)
        
def solve():
    n = inp()
    mapping = {i: Node(i) for i in range(1, n + 1)}
    dag_mapping = {i: DagNode(i) for i in range(1, n + 1)}
    
    for _ in range(n - 1):
        s, d = sorted(mul())
        mapping[d].add_edge(mapping[s])
        mapping[s].add_edge(mapping[d])
    
    queue = deque([mapping[1]])
    
    # Root tree.
    visited = set()
    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        for neighbor in node.edges:
            if neighbor in visited:
                continue
            dag_mapping[neighbor.val].add_prev(dag_mapping[node.val])
            dag_mapping[node.val].add_child(dag_mapping[neighbor.val])
            queue.append(neighbor)
    
    red = 0
    blue = 0

    queue = deque([(dag_mapping[1], True)])
    
    

    while queue:
        node, is_red = queue.popleft()
        if is_red:
            red += 1
        else:
            blue += 1

        for child in node.children:
            queue.append((child, not is_red))
    
    return (red) * (red - 1) + (blue) * (blue - 1)
    
print(solve())