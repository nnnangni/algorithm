def dfs(i,j,cnt,length):
    global arr, K, N, maxlen, visited
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    if length>maxlen:
        maxlen = length
    visited[i][j]=1
    for n in range(4):
        ni = i + di[n]
        nj = j + dj[n]
        if 0<=ni<N and 0<=nj<N:
            if visited[ni][nj]==0:
                if arr[i][j]>arr[ni][nj]:
                    dfs(ni,nj,cnt,length+1)
                elif arr[i][j]>arr[ni][nj]-K and cnt!=0:
                    origin = arr[ni][nj]
                    arr[ni][nj] = arr[i][j]-1
                    dfs(ni,nj,0,length+1)
                    arr[ni][nj] = origin
    visited[i][j]=0

T = int(input())
for tc in range(T):
    N, K = map(int,input().split())
    arr = [list(map(int,input().split())) for i in range(N)]
    visited = [[0] * N for i in range(N)]
    maxh = 0
    maxlen = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j]>maxh:
                maxh = arr[i][j]
    for i in range(N):
        for j in range(N):
            if arr[i][j]==maxh:
                dfs(i,j,1,1)

    print('#{} {}'.format(tc+1, maxlen))