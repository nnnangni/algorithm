T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    matrix = [list(input().split()) for i in range(N)]
    for y in range(N):
        for x in range(N):
            if matrix[y][x:x+M/2] == matrix[y][N-x-1:M/2:-1]:
                print(matrix[y][x:x+M-1])

