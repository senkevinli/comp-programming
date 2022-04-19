import sys
import math
import bisect
from sys import stdin,stdout
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd
from bisect import bisect_left as bl,bisect_right as br


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


def form_query(start, end):
    print(f'? {start + 1} {end + 1}')
    stdout.flush()
    return inp()

rooms = inp()

biggest_range = None
second_biggest_range = None

low = 0
high = rooms - 1


second_big = rooms - 1
queries = 0


# while low < high:
    
#     midpoint = (low + high) // 2
    
#     left_big = form_query(low, midpoint)
#     right_big = form_query(midpoint + 1, high)
    
#     queries += 2
    
#     assert queries <= 40    
#     if left_big > right_big:
        
#         if right_big > second_big:
#             second_big = right_big
#             second_biggest_range = (midpoint + 1, high)
#         high = midpoint
#     else:
#         if left_big > second_big:
#             second_big = left_big
#             second_biggest_range = (low, midpoint)
#         low = midpoint + 1
        
# low, high = second_biggest_range

while low < high:
    midpoint = (low + high) // 2
    queries += 2
    assert queries <= 40
    left_big = form_query(low, midpoint)
    right_big = form_query(midpoint + 1, high)
    
    
    if left_big == second_big:
        high = midpoint
        continue
    
    if right_big == second_big:
        low = midpoint + 1
        continue
    
    if left_big > second_big:
        high = midpoint
    else:
        low = midpoint + 1


print(f'! {low + 1}')