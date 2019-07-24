def bfs(a,b):
    global arr, visited, day, queuex, queuey
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if nx>=0 and ny>=0 and nx<N and ny<M:
            if arr[nx][ny]==0 and visited[nx][ny]==0:
                arr[nx][ny]=1
                visited[nx][ny]=1
                queuex.append(nx)
                queuey.append(ny)
                day += 1

M,N = map(int, input().split())
arr = []
visited = []
queuex=[]
queuey=[]
day = 0
for v in range(N):
    visited.append([0]*M)
for i in range(N):
    arr.append(list(map(int,input().split())))
for nidx, nval in enumerate(arr):
    for midx, mval in enumerate(nval):
        if mval==1:
            queuex.append(nidx)
            queuey.append(midx)
while queuex and queuey:
    bfs(queuex.pop(0),queuey.pop(0))



# print(day)

