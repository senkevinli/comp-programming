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

def prefix_sum(arr):
    for i in range(1, len(arr)):
        arr[i] += arr[i-1]
    return arr

class Node:
    def __init__(self, val):
        self.value = val
        self.children = []
        self.in_deg = 0
        
    
    def add_adj(self, node):
        self.children.append(node)
        node.in_deg += 1

    def __str__(self):

        last_holder = '   '
        holder = '│  '
        mid_marker = '├──'
        end_marker = '└──'

        ret = ''
        ret += str(self.value) + '\n'
        
        for i in range(len(self.children)):
            marker = mid_marker if i < len(self.children) - 1 else end_marker
            padder = holder if i < len(self.children) - 1 else last_holder
            
            sub = str(self.children[i])
            
            lines = [line for line in sub.split('\n') if line]
            
            ret += marker + lines[0] + '\n'
            
            if len(lines) > 1:
                ret += '\n'.join(padder + line for line in lines[1:]) + '\n'
        
        return ret
def solve():
    n = inp()
    arr = seq()
    
    mapping = { i: Node(i) for i in range(1, n + 1) }
    for i, a in enumerate(arr):
        parent = mapping[a]
        child = mapping[i + 2]
        
        parent.add_adj(child)
    
    root = mapping[1]
    
    inner_nodes = [ node for node in mapping.values() if len(node.children) > 0 ]
    
    inner_nodes.sort(key = lambda x: len(x.children), reverse = True)
    node_children = []
    infected = len(inner_nodes) + 1
    for node in inner_nodes:
        if len(node.children) - infected > 0:
            node_children.append(len(node.children) - infected)
        infected -= 1

    if len(node_children) == 0:
        return len(inner_nodes) + 1   

    infected = len(inner_nodes) + 1
    while True:
        maxi = -math.inf
        maxi_index = -1
        for i in range(len(node_children)):
            node_children[i] -= 1
            
            if node_children[i] > maxi:
                maxi = node_children[i]
                maxi_index = i
        
        node_children[maxi_index] -= 1
        infected += 1
        
        if node_children[maxi_index] <= 0:
            break
    
    return infected
        
        
    

cases = inp()
for _ in range(cases):
    print(solve())