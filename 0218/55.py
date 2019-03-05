N = int(input())
A = [list(map(int, input().split())) for i in range(N)]

di = [0,1,0,-1]
dj = [1,0,-1,0]
i = 1
j = 1
sumall = 0
for i in range(N):
    for j in range(N):
        # print(i, j, end=' ')
        sum = 0
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni>=0 and ni<N and nj>=0 and nj<N:
                sum += (abs(A[ni][nj]-A[i][j]))
        sumall += sum
print(sumall)

