L = int(input())
N = int(input())
cake=[0]*L
exp = []
for i in range(N):
    a, b = map(int,input().split())
    exp.append(b-a)
    for k in range(a,b+1):
        if cake[k-1]==0:
            cake[k-1]=i+1

cakelist = []
for n in range(N):
    cakelist.append(cake.count(n+1))

max=0
for idx, val in enumerate(exp):
    if val>max:
        max=val
        num=idx

max2=0
for idx, val in enumerate(cakelist):
    if val>max2:
        max2=val
        num2=idx

print(num+1)
print(num2+1)




