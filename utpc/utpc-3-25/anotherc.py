def gcd(a, b):
    while b:
        a %= b
        a, b = b, a
    return a
 
 
n = int(input())
thing = list(map(int, input().split()))
thing.sort()
res = thing[0]
for i in thing[1:]:
    res = gcd(i, res)
num = thing[-1] // res - n
if num & 1 == 0:
    print('Davy Jones')
else:
    print('Jack Sparrow')