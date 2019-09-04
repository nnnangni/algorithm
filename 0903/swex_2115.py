def f():
    global M
    maximum = 0
    for m in range(1,2**M):
        setsum = 0
        honeysum = 0
        for n in range(M):
            if m & (1<<n)!=0 and setsum+case[n]<=C:
                setsum += case[n]
                honeysum += case[n] * case[n]
        if maximum < honeysum:
            maximum = honeysum
    return maximum

T = int(input())
for tc in range(1,T+1):
    N, M, C = map(int,input().split())
    arr = [list(map(int,input().split())) for i in range(N)]
    result = []
    for i in range(N):
        col = []
        for j in range(N):
            case = []
            for k in range(M):
                if j<=N-M:
                    case.append(arr[i][j+k])
            if len(case) == M:
                col.append(f())
        result.append(max(col))
    result.sort(reverse=True)
    ans = result[0]+result[1]
    print("#{} {}".format(tc,ans))

