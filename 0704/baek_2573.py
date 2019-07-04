n, T = map(int,input().split())
numbers = list(map(int,input().split()))
sum = 0
cnt = 0
while sum<=T:
    sum += numbers[cnt]
    if sum>T:
        break
    cnt += 1
print(cnt)