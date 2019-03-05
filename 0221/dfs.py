# input
# 마지막 정점번호 주어짐 : 7 (v)
# edge의 갯수 : 8 (e)
# 이러한 간선으로 구성됨 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
# 그래프에 대한 입력정보는 이러한 형식으로 주어짐.
# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

def dfs(n, v):
    stack = []
    visited = [0]*(v+1) # v번 노드까지 방문표시
    visited[n] = 1
    stack.append(n)
    #스택이 비어있지 않은 동안 계속 탐색
    while len(stack)!=0:
        n = stack.pop() # 스택에 있는 애를 꺼냄
        print(n, end=' ') # 방문순서
        #for i in range(1, v+1):
        for i in range(v, 0, -1):
            # n행에 대해서 i번 노드가 인접이고, 방문하지 않은 노드면
            if adj[n][i]!=0 and visited[i]==0:
                # 내가 갈 수 있는 곳들을 저장
                stack.append(i)
                visited[i] = 1


V, E = map(int, input().split())
edge = list(map(int, input().split()))

# 인접행렬 저장하기
adj = [[0]*(V+1) for i in range(V+1)]
for i in range(E):
    n1 = edge[i*2]
    n2 = edge[i*2+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1 # 12 랑 21이 연결되어있음 -> 방향성이 없는 그래프

dfs(1, V)