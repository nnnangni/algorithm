# 0~9 까지의 정수
# 4 5 6 7 8 9
a = list(map(int, input().split()))
b = int(input())
cnt = [0]*10 # 0부터 9까지의 갯수 저장

for i in range(6):
    cnt[a[i]] += 1

print(cnt)
print(b)