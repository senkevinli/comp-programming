import sys
import math
import bisect
from sys import stdin,stdout
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd
from bisect import bisect_left as bl,bisect_right as br

LINES = sys.stdin.read().splitlines()[::-1]
def input(): return LINES.pop()

# single integer
inp = lambda: int(input())

fl_seq = lambda: list(map(float,input().strip().split()))


def fill_dp(n, dp, grid):
    
    # track indices.
    cur = []
    idx = 1
    
    # store original n
    tmp = n
    
    # iterate through bits, 1 => raisin at index is present in subset.
    while n > 0:
        if n & 1 == 1:
            cur.append(idx - 1)
        
        idx += 1
        n >>= 1

    # base case where only raisin left, always winnable.
    if len(cur) == 1:
        dp[tmp][cur[0]] = 1
        return
    
    # n choose 2 different pairs of raisins to battle.
    total = (len(cur) * (len(cur) - 1)) // 2
    chance_select = 1 / total

    
    for i in range(len(cur)):
        for j in range(i + 1, len(cur)):
            # two different raisins.
            a = cur[i]
            b = cur[j]
            
            # prob that b loses.
            prob_b = grid[a][b]
            
            # leftover state when b loses.
            left_b = tmp & ~ (1 << b)
            
            # prob that a loses.
            prob_a = grid[b][a]
            
            # leftover state when a loses.
            left_a = tmp & ~ (1 << a)

            assert prob_a + prob_b == 1.0

            # total probability.
            for k in range(len(dp[tmp])):
                dp[tmp][k] += chance_select * dp[left_a][k] * prob_a
                dp[tmp][k] += chance_select * dp[left_b][k] * prob_b
        
    
            

def solve():
    raisins = inp()
    
    grid = []
    for i in range(raisins):
        grid.append(fl_seq())

    # keeping track of win probabilities for all subsets. dp[x][y] = prob that 
    # raisin y wins for the subset x.
    dp = [[0 for _ in range(raisins)] for i in range(2 ** raisins)]

    # iterate through all possible subsets.
    for i in range(1, 2 ** raisins):
        fill_dp(i, dp, grid)
    
    for elem in dp[-1]:
        print(elem)
        
cases = 1
for _ in range(cases):
    solve()