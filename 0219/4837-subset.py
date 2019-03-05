T = int(input())
A = [1,2,3,4,5,6,7,8,9,10,11,12]
for tc in range(1,T+1):
    N, K = map(int, input().split())
    count = 0
    for i in range(2**12):
        list = []
        for j in range(12):
            if i&(1<<j)!=0:
                list.append(A[j])
        if sum(list) == K and len(list)==N:
            count += 1
    print(f"#{tc} {count}")
