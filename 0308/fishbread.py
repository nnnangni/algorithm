import sys
sys.stdin = open('fishinput.txt','r')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    fish = 0
    sold = {}
    for m in range(M):
        t, c = map(int, input().split())
        sold[t] = c
    result = 0
    for i in range(1,61):
        fish += 2
        if i in sold.keys():
            fish -= sold[i]
            if fish<=0:
                fish = -1
                break
    print(fish)


