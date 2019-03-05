import sys
sys.stdin=open("input (10).txt","r")

def column(matrix, i):
    return [row[i] for row in matrix]

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for n in range(N)]
    cnt = 0

    for i in range(N):
        col = column(arr, i)
        for j in range(N-1):
            if col[j]==1 and col[j+1]!=2:
                col[j+1]=1
                col[j]=0
            elif col[j]==1 and col[j+1]==2:
                cnt += 1

