def bfs(x,y,newc):
    global color, visited, queue
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    queue.append([x,y])
    while queue:
        s = queue.pop(0)
        for d in range(4):
            nx = s[0] + dx[d]
            ny = s[1] + dy[d]
            if 0<=nx<N and 0<=ny<N:
                if arr[nx][ny]== newc and visited[nx][ny]==0:
                    queue.append([nx,ny])
                    visited[nx][ny]=1
    color[c] += 1

N = int(input())
arr = [list(map(str,input())) for i in range(N)]
queue = []
count = 0
visited = [[0 for i in range(N)] for j in range(N)]
color = {'R':0,'G':0,'B':0}
for r in range(N):
    for s in range(N):
        for c in color:
            if arr[r][s] == c and visited[r][s]==0:
                visited[r][s]=1
                bfs(r,s,c)

three = sum(color.values())

for n in range(N):
    for m in range(N):
        if arr[n][m]=="G":
            arr[n][m] = "R"

queue = []
count = 0
visited = [[0 for i in range(N)] for j in range(N)]
color = {'R':0,'B':0}
for r in range(N):
    for s in range(N):
        for c in color:
            if arr[r][s] == c and visited[r][s]==0:
                visited[r][s]=1
                bfs(r,s,c)

two = sum(color.values())

print(three,two)



