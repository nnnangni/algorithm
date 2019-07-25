import re

def f1(x):
    return x[1]
def f2(x):
    return x[1][1]
def f3(x):
    return x[0]

N = int(input())
serial = []
newserial = {}
for i in range(N):
    serial.append(input())
for l in serial:
    newserial[l]=[len(l)]
for k in newserial:
    numbers = re.findall("\d", k)
    sum = 0
    for p in numbers:
        sum += int(p)
    newserial[k].append(sum)
res = sorted(newserial.items(),key=f3)
res2 = sorted(res, key=f2)
res3 = sorted(res2, key=f1)
for ans in res3:
    print(ans[0])
print(res3)

