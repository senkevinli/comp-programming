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


from queue import PriorityQueue

class Node:
    def __init__(self, val):
        self.val = val
        self.adj = []
    
    def add_adj(self, cost, n):
        self.adj.append((cost, n))
    
    def __lt__(self, other):
        return self.val < other.val
    # def __hash__(self):
    #     pass

def dijkstra(start_vertex, all_nodes):
    visited = set()
    D = { v:float('inf') for v in all_nodes }
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (_, current_vertex) = pq.get()
        visited.add(current_vertex)

        for neighbor in current_vertex.adj:
            distance, node = neighbor
            if node not in visited:
                old_cost = D[node]
                new_cost = D[current_vertex] + distance
                
                if new_cost < old_cost:
                    pq.put((new_cost, node))
                    D[node] = new_cost
    return D

def solve():
    num_nodes = inp()
    
    items = seq()
    
    edges = inp()
    
    for _ in range(edges):
        src, dest, cost = seq()
        
        


solve()
