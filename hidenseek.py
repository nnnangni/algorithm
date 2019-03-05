def bfs(x,k):
    q=[]
    visited = [0]*(100001)
    q.append(x)
    visited[x] = 1
    while len(q) != 0:
        x = q.pop(0)
        if x==k:
            return visited[k]-1
        # x-1 인접
        if x-1>=0 and visited[x-1]==0:
            q.append(x-1)
            visited[x-1] = visited[x]+1
        # x+1 인접

        # 2*x 인접접
