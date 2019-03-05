N = 3
A = [[1,2,3],[4,5,6],[7,8,9]]
# 오른쪽부터 시계방향으로
di = [0,1,0,-1]
dj = [1,0,-1,0]
i = 1
j = 1
for i in range(N):
    for j in range(N): # 배열 A의 모든 원소에 대해
        print(i, j, end= ' ')
        for k in range(4): # k번 방향 탐색
            ni = i + di[k]
            nj = j + dj[k]
            # 새로운 좌표에서 유효한 범위만 출력
            if ni>=0 and ni<N and nj>=0 and nj<N:
                print(A[ni][nj], end=' ')
        print()


