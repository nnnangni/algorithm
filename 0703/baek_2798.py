from itertools import combinations
N,M = map(int,input().split())
card = list(map(int,input().split()))
sumlist = []
for s in list(combinations(card,3)):
    sum = 0
    for j in s:
        sum += j
    sumlist.append(sum)

max = 0
for i in sumlist:
    if i<=M and i>=max:
        max = i
print(max)


