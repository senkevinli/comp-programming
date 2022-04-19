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

def flip_sequence(sequence, flip):
    if not flip:
        return sequence
    
    return ['1' if s == '0' else '0' for s in sequence]

def solve():
    n, k = mul()
    
    sequence = strl()
    moves = [0] * n
    
    leftover = k
    flip = False
    answer = []
    for i, s in enumerate(sequence):
        
        if leftover == 0:
            break
        
        letter = s
        if flip:
            letter = '1' if s == '0' else '0'
            
        if i == len(sequence) - 1:
            moves[i] += leftover
            answer.append(letter)
            break
        if letter == '1':
            if leftover % 2 == 1:
                flip = not flip
                leftover -= 1
                moves[i] += 1
        else:
            if leftover % 2 == 0:
                flip = not flip
                leftover -= 1
                moves[i] += 1
        answer.append('1')
    

    
    flip = k % 2 != 0
    best = answer + flip_sequence(sequence[len(answer):], flip)
    print(''.join(best))
    print(" ".join(map(str, moves)))
    

cases = inp()

for _ in range(cases):
    solve()