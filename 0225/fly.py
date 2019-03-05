T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for n in range(N)]

    new_list = []
    for k in range(N-M+1):
        for q in range(N-M+1):
            new_sum = 0
            for i in range(M):
                for j in range(M):
                    new_sum += arr[k+i][q+j]
                    print(k,i,q,j)
                    print(k+i, q+j)
            new_list.append(new_sum)
    ans = max(new_list)

