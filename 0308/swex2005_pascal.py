import sys
sys.stdin = open('2005input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    pascal = []
    for i in range(1,N+1):
        pascal.insert(i, [1]*i)

    if N>=3:
        for j in range(2,N):
            for k in range(1,j):
                pascal[j][k] = pascal[j-1][k-1]+pascal[j-1][k]

    print('#{}'.format(tc))
    for p in range(len(pascal)):
        for q in range(p+1):
            print(pascal[p][q],end=' ')
        print()
