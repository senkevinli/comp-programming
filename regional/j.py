import sys
import math
import bisect
from sys import stdin,stdout
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd
from bisect import bisect_left as bl,bisect_right as br
from collections import deque

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
        self.edges = []
    
    def add_edge(self, n):
        self.edges.append(n)

class DagNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        
    def add_prev(self, p):
        self.prev = p
        
        

def solve():
    # Implementation goes here.
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
            queue.append(neighbor)
    permutations = []
    
    for _ in range(n):
        permutations.append(inp())
        
    for i in range(n - 1):
        cur = permutations[i]
        next = permutations[i + 1]
        
        cur_node = dag_mapping[cur]
        next_node = dag_mapping[next]
        
        one = check_one(cur_node, next_node)
        two = check_two(cur_node, next_node)
        three = check_three(cur_node, next_node)
        
        if not (one or two or three):
            return 0
    return 1
    

def check_one(n1, n2):
    a = is_parent(n1, n2)
    b = is_parent(n2, n1)

    return a or b

def check_two(n1, n2):
    a = is_grandparent(n1, n2)
    b = is_siblings(n1, n2)
    c = is_grandparent(n2, n1)
    
    return a or b or c

def check_three(n1, n2):
    a = is_great_grandparent(n1, n2)
    b = is_great_grandparent(n2, n1)
    c = is_avuncular(n1, n2)
    d = is_avuncular(n2, n1)

    return a or b or c or d


def is_parent(n1, n2):
    return n1 is not None and n2 is not None and n1.prev is not None and n1.prev == n2

def is_siblings(n1, n2):
    return n1 is not None and n2 is not None and n1.prev is not None and n2.prev is not None and n1.prev == n2.prev

def is_grandparent(n1, n2):
    return n1 is not None and n2 is not None and n1.prev is not None and n1.prev.prev  is not None and n1.prev.prev == n2

def is_great_grandparent(n1, n2):
    ret = n1 is not None and n2 is not None and n1.prev is not None and n1.prev.prev is not None and n1.prev.prev.prev is not None and n1.prev.prev.prev == n2
    return ret

def is_avuncular(n1, n2):
    return n1 is not None and n2 is not None and n1.prev is not None and n2.prev is not None and n1.prev.prev is not None and n1.prev.prev == n2.prev


cases = inp()

for _ in range(cases):
    print(solve())