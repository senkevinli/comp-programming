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

def solve():
    length = inp()
    
    numbers = strwords()
    
    
    for i in range(length):
        if i - 1 >= 0:
            ret = make_smaller(numbers[i], numbers[i - 1])
            if ret is not None:
                numbers[i] = str(ret)
                print(' '.join(numbers))
                return
        
        if i + 1 < length:
            ret = make_bigger(numbers[i], numbers[i + 1])
            if ret is not None:
                numbers[i] = str(ret)
                print(' '.join(numbers))
                return
    
    print('impossible')
                
        

def make_bigger(left, right):
    
    right_int = int(right)
    
    numbers = [ str(i) for i in range(10) ]
    digits = list(left)
    for i in range(len(digits)):
        for n in numbers:
            if i == 0 and n == '0' and len(digits) != 1:
                continue
            saved = digits[i]
            digits[i] = n
            transformed = int(''.join(digits))
            if transformed > right_int:
                return transformed
            digits[i] = saved
    return None



def make_smaller(left, right):
    
    right_int = int(right)
    
    numbers = [ str(i) for i in range(10) ]
    digits = list(left)
    for i in range(len(digits)):
        for n in numbers:
            if i == 0 and n == '0' and len(digits) != 1:
                continue
            saved = digits[i]
            digits[i] = n
            transformed = int(''.join(digits))
            if transformed < right_int:
                return transformed
            digits[i] = saved
    return None
            
                
    

solve()