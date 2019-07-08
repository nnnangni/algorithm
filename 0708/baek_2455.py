total = 0
numlist = []
for i in range(4):
    O, I = map(int, input().split())
    total -= O
    total += I
    numlist.append(total)
print(max(numlist))