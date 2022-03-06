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
area = lambda *p: abs(sum(i[0] * j[1] - j[0] * i[1] for i, j in zip(p, p[1:] + p[:1]))) / 2
dist = lambda p1, p2: sum((a - b) * (a - b) for a, b in zip(p1, p2))**0.5



def solve():
    n = inp()
    
    points = []
    for i in range(n):
        points.append(tuple(mul()))

    right_vertex = points[1]
    left_vertex = points[-1]
    
    prev = right_vertex
    total = 0
    arr = [0]
    for i in range(2, len(points)):
        d = dist(prev, points[i])
        total += d
        arr.append(total)
        prev = points[i]
        
    lo = 0
    hi = total
    
    total_area = area(*points)
    abs_prec = 1e-9
    while abs(hi - lo) > abs_prec:
        mi = lo + (hi - lo) / 2
        if area_comparison(mi, points, arr, total_area):
            hi = mi
        else:
            lo = mi

    mid = (lo + hi) / 2
    
    point = convert_to_point(points, mid, arr)[-1]
    
    return point
        
    
    
def convert_to_point(points, dist, arr):
    start_idx = binary_search_arr(arr, dist, 0, len(arr))
    
    leftover = dist - arr[start_idx]
    
    p = leftover / (arr[start_idx + 1] - arr[start_idx])
    
    
    x_i, y_i = points[start_idx + 1]
    x_f, y_f = points[start_idx + 2]
    
    y = y_i + p*(y_f - y_i)
    x = x_i + p*(x_f - x_i)
    
    
    return points[0:start_idx + 2] + [(x, y)]

def area_comparison(dist, points, arr, total_area):
    right_half = convert_to_point(points, dist, arr)
    
    right_half_area = area(*right_half)
    return right_half_area > (total_area - right_half_area)
    
 
def binary_search_arr(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # If the target is found, return the mid index.
        if array[mid] == target:
            return mid
        # If the value of the mid index is greater than the target, search the left part.
        elif array[mid] > target:
            end = mid - 1
        # If the value of the mid index is smaller than the target, search the right part.
        else:
            start = mid + 1
    return end

result = solve()

print(f'{result[0]} {result[1]}')
