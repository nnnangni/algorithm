def paint(r1,c1,r2,c2,color):
    c = 0
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            A[i][j] = color+A[i][j]
            if A[i][j] == 3:
                c = c+1
    return c

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    A = [[0] * 10 for i in range(10)]
    count = 0
    for i in range(0,N):
        r1, c1, r2, c2, color = map(int, input().split())
        count = count + paint(r1,c1,r2,c2,color)
    print(f"#{tc} {count}")


