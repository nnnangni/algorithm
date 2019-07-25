def bfs(a,b):
    global arr, visited, queue, front
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if nx>=0 and ny>=0 and nx<N and ny<M:
            if arr[nx][ny]==0 and visited[nx][ny]==0:
                # 날짜를 세어주는 대신 행렬 값을 바꾸기
                arr[nx][ny] = arr[a][b]+1
                visited[nx][ny]=1
                # 큐에 새로 넣어주고 큐의 인덱스도 이동하는 작업
                front += 1
                queue[front] = nx
                front += 1
                queue[front] = ny

M,N = map(int, input().split())
arr = []
visited = []
# 최대 크기의 큐 생성
queue = [0]*M*N*2
# 인덱스 값인 front와 rear 생성
front = -1
rear = -1
for v in range(N):
    visited.append([0]*M)
for i in range(N):
    arr.append(list(map(int, input().split())))
for p in range(N):
    for q in range(M):
        if arr[p][q] == 1:
            # 1인 값을 모두 queue에 넣어주는 작업
            front += 1
            queue[front] = p
            front += 1
            queue[front] = q

# pop 대신 rear을 활용해서 하나씩 값을 가져옴
while front!=rear:
    rear += 1
    i = queue[rear]
    rear += 1
    j = queue[rear]
    # 좌표를 가지고 함수 실행
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

