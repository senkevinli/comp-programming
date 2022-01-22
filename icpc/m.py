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
    # Implementation goes here.
    num = strng()
    
    num = bin(int(num, 8))[2:]
    
    if len(num) < 19:
        num = ('0' * (19 - len(num))) + num
    
    num = num[::-1]
    grid = [[0, 0, 0] for _ in range(3)]
    
    played = num[:9]
    xs = num[9:-1]
    turn = num[-1]
    
    # 0 for O, 1 for X, 2 for empty
    idx = 0
    for i in range(3):
        for j in range(3):
            play = played[idx]
            type = xs[idx]
            
            if play == '1':
                grid[i][j] = type
            else:
                grid[i][j] = '2'
            idx += 1
    
    for i in range(3):
        if grid[i].count('0') == 3:
            print('O wins')
            return
        elif grid[i].count('1') == 3:
            print('X wins')
            return
    
    for i in range(3):
        col = [grid[0][i], grid[1][i], grid[2][i]]  
        if col.count('0') == 3:
            print('O wins')
            return
        elif col.count('1') == 3:
            print('X wins')
            return
    
    diag = [grid[0][0], grid[1][1], grid[2][2]]
    if diag.count('0') == 3:
        print('O wins')
        return
    elif diag.count('1') == 3:
        print('X wins')
        return

    diag2 = [grid[0][2], grid[1][1], grid[2][0]]
    if diag2.count('0') == 3:
        print('O wins')
        return
    elif diag2.count('1') == 3:
        print('X wins')
        return
    
    if played == '111111111':
        print("Cat's")
        return
    
    print('In progress')
    # print(played, xs, turn)
    
    

cases = inp()

for i in range(cases):
    solve()