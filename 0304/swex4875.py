# 4875. [파이썬 S/W 문제해결 기본] 5일차 - 미로

def miro(i,j,n):
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    # 목적지에 도착한 경우
    if maze[i][j] == 3:
        return 1
    else:
        # 방문한 칸으로 미로에 직접 표시
        maze[i][j] = 1
        # 주변 칸으로 이동가능한지 검사
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            # 미로를 벗어나지 않으면
            if ni>=0 and ni<n and nj>=0 and nj<n:
                # ni, nj칸이 벽이 아니면 이동
                if maze[ni][nj]!=1:
                    r = miro(ni, nj, n)
                    # 목적지에 도착한 경우
                    if r==1:
                        return 1
        # 가능한 모든 방향에서 목적지를 찾지 못하면
        return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 현재위치 i,j
    # 벽이 아니면 && 지나가지 않은 칸이면 (i,j+1 i+1,j i,j-1 i-1,j) 로 이동
    # 문자열로 저장하는 경우 방문표시 배열
    maze = [list(map(int, input()) for i in range(N))]
    startI = -1
    startJ = -1
    for i in range(N):
        for j in range(N):
            if maze[i][j]==2:
                startI = i
                startJ = j
                break
        if(startI!=-1):
            break
    print('#{} {}'.format(tc,miro(i,j,N)))