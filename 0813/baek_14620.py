import itertools

# m개의 원소를 찾는 부분집합 구하기
def findsubsets(S,m):
    return set(itertools.combinations(S, m))

N = int(input())
field = [list(map(int, input().split())) for i in range(N)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
# 꽃의 중점과 4방향의 합 -> plist
plist = {}
for i in range(N):
    for j in range(N):
        price = 0
        cnt = 0
        price+=field[i][j]
        for n in range(4):
            nx = i + dx[n]
            ny = j + dy[n]
            if 0<=nx<N and 0<=ny<N:
                price += field[nx][ny]
                cnt += 1
        if cnt==4:
            plist[i,j] = price

# 딕셔너리를 리스트로 변환
flower = plist.items()

minlist = []

threefield = findsubsets(flower,3)
for i in threefield:
    visited = [[0 for k in range(N)] for j in range(N)]
    sumprice = []
    for j in i:
        visitcnt = 0
        fourcnt = 0
        for n in range(4):
            idx = j[0][0] + dx[n]
            idy = j[0][1] + dy[n]
            if visited[idx][idy] == 0:
                visitcnt += 1
        # 만약 네방향 모두 방문한 적 없는 좌표라면
        if visitcnt == 4:
            visited[j[0][0]][j[0][1]] = 1
            for n in range(4):
                idx = j[0][0] + dx[n]
                idy = j[0][1] + dy[n]
                if visited[idx][idy] == 0:
                    fourcnt += 1
                    visited[idx][idy] = 1
        if fourcnt == 4:
            sumprice.append(j[1])
    if len(sumprice)==3:
        minlist.append(sum(sumprice))

print(min(minlist))