def bfs(a,b):
    global arr, visited, queue, front
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if nx>=0 and ny>=0 and nx<N and ny<M:
            if arr[nx][ny]==0 and visited[nx][ny]==0:
                arr[nx][ny] = arr[a][b]+1
                visited[nx][ny]=1
                front += 1
                queue[front] = nx
                front += 1
                queue[front] = ny

M,N = map(int, input().split())
arr = []
visited = []
queue = [0]*M*N*2
front = -1
rear = -1
for v in range(N):
    visited.append([0]*M)
for i in range(N):
    arr.append(list(map(int, input().split())))
for p in range(N):
    for q in range(M):
        if arr[p][q] == 1:
            front += 1
            queue[front] = p
            front += 1
            queue[front] = q

while front!=rear:
    rear += 1
    i = queue[rear]
    rear += 1
    j = queue[rear]
    bfs(i,j)

amax=0
for a in arr:
    for b in a:
        if b>=amax:
            amax = b
zero = []
for a in arr:
    for b in a:
        zero.append(b)
if 0 in zero:
    amax=0

print(amax-1)

