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

def solve(visited, num):
    
    if len(visited) == 10:
        print('Impossible')
        return
    
    if '0' not in visited and len(visited) == 9:
        print(0)
        return

    if num == '1':
        print(0, 2)
        return
    
    ascending = [str(i) for i in range(10) if str(i) not in visited]
    
    # print(ascending)
    
    # greater (same digits)
    
    significant = None
    digits = len(num)

    for str_num in ascending:
        if int(num[0]) < int(str_num):
            significant = str_num
            break
    else:
        # adding a digit
        digits += 1
        for str_num in ascending:
            if int(str_num) == 0:
                continue
            significant = str_num
            break
    
    high_result = significant + (ascending[0] * (digits - 1))
    
    
    # smaller (same digits)
    
    significant = None
    digits = len(num)
    
    for str_num in ascending[::-1]:
        if str_num != '0' and (int(num[0]) > int(str_num)):
            significant = str_num
            break
    else:
        # removing a digit
        digits -= 1
        significant = ascending[-1]

    low_result = significant + (ascending[-1] * (digits - 1))

    low_result = int(low_result)
    high_result = int(high_result)
    
    diff_1 = abs(int(num) - low_result)
    diff_2 = abs(int(num) - high_result)

    if diff_1 == diff_2:
        print(low_result, high_result)
    elif diff_1 > diff_2:
        print(high_result)
    else:
        print(low_result)
        
    
    


num = strng()

visited = set([c for c in num])

solve(visited, num)
