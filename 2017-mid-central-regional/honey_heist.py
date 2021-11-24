import sys
import math
import bisect
from sys import stdin,stdout
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd
from collections import deque
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

def solve():
    # Implementation goes here.
    
    r, n, a, b, x = mul()
    hardened = seq()

    mapping = dd(lambda : Node(0))

    # ascending
    val = 0
    for i in range(r - 1):
        for j in range(r + i):
            val += 1
            below_left = val + r + i
            below_right = val + r + i + 1

            mapping[val].adj.append(mapping[below_left])
            mapping[val].adj.append(mapping[below_right])
            mapping[below_left].adj.append(mapping[val])
            mapping[below_right].adj.append(mapping[val])

            mapping[val].val = val
            mapping[below_left].val = below_left
            mapping[below_right].val = below_right
            if j != 0:
                mapping[val].adj.append(mapping[val - 1])
                mapping[val - 1].adj.append(mapping[val])


    for i in range(r - 1, -1, -1):
        for j in range(r + i):
            val += 1
            if i != 0:
                below_left = val + r + i - 1
                below_right = val + r + i

                if j == 0:
                    mapping[val].adj.append(mapping[below_right])
                    mapping[below_right].adj.append(mapping[val])

                    mapping[val].val = val
                    mapping[below_right].val = below_right
                elif j == r + i - 1:
                    mapping[val].adj.append(mapping[below_left])
                    mapping[below_left].adj.append(mapping[val])

                    mapping[val].val = val
                    mapping[below_left].val = below_left
                else:
                    mapping[val].adj.append(mapping[below_left])
                    mapping[val].adj.append(mapping[below_right])
                    mapping[below_left].adj.append(mapping[val])
                    mapping[below_right].adj.append(mapping[val])

                    mapping[val].val = val
                    mapping[below_left].val = below_left
                    mapping[below_right].val = below_right
            
            if j != 0:
                mapping[val].adj.append(mapping[val - 1])
                mapping[val - 1].adj.append(mapping[val])
    
    # for val in mapping:
    #     print(val)
    #     for a in mapping[val].adj:
    #         print(a.val)
    #     print()

    queue = deque([(mapping[a], 0)])
    visited = set()

    while queue:
        cur, dist = queue.popleft()
        if cur in visited or dist > n or cur.val in hardened:
            continue
        visited.add(cur)

        if cur.val == b:
            return dist
        for a in cur.adj:
            queue.append((a, dist + 1))
    
    return -1


result = solve()
if result == -1:
    print('No')
else:
    print(result)