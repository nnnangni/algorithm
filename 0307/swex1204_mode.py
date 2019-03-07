import sys
sys.stdin = open('1204input.txt','r')


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    score = list(map(int, input().split()))
    mode = {}
    for i in score:
        if i in mode:
            mode[i] += 1
        else:
            mode[i] = 1

    maxs = {}
    for idx, val in mode.items():
        if val == max(mode.values()):
            maxs[idx] = val
    print('#{} {}'.format(tc, max(maxs.keys())))

