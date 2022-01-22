n = int(input())
count = 0
answers = []
first = True
val = 0
while count < n:
    if first:
        val = int(input())
        first = False
    else:
        cur = int(input())
        if cur % val == 0:
            answers.append(cur)
            first = True
    count += 1
for x in answers:
    print(x)