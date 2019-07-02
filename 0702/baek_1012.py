def bfs(a,b):
    global M, N, visited, cnt
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    q = []
    q.append([a, b])
    while q:
        s = q.pop()
        for i in range(4):
            nx = s[0] + dx[i]
            ny = s[1] + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < M :
                if field[nx][ny]==1 and visited[nx][ny]==0:
                    q.append([nx, ny])
                    visited[nx][ny]=1

T = int(input())
for i in range(T):
    M, N, K = map(int,input().split())
    field = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    cnt = 0
    for j in range(K):
        x, y = map(int,input().split())
        field[y][x]=1

    for a in range(N):
        for b in range(M):
            if field[a][b]==1 and visited[a][b]==0:
                visited[a][b]=1
                bfs(a,b)
                cnt += 1
    print(cnt)

