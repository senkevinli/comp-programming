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

def convert_letter_to_number(letter):
    return ord(letter) - ord('a')

class Trie:
    
    def __init__(self):
        self.struct = [[0] * 11 for _ in range(11)]
        
    def add_word(self, word):
        curr = self.struct
        first_index = convert_letter_to_number(word[0])
        second_index = convert_letter_to_number(word[1])
        
        self.struct[first_index][second_index] += 1
    
    def combos(self):
        total = 0
        for row in self.struct:
            
            non_zeroes = []
            for n in row:
                if n != 0:
                    non_zeroes.append(n)
            
            for i in range(len(non_zeroes)):
                for j in range(i + 1, len(non_zeroes)):
                    total += non_zeroes[i] * non_zeroes[j]
        
        return total

def solve():
    n = inp()
    
    forward = Trie()
    backward = Trie()

    for _ in range(n):
        s = strng()
        forward.add_word(s)
        backward.add_word(s[::-1])
    
    return forward.combos() + backward.combos()

cases = inp()
for _ in range(cases):
    print(solve())