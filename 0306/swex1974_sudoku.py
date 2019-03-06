import sys
sys.stdin = open('1974input.txt','r')

T = int(input())
for tc in range(1,T+1):
    puzzle = list(input().split() for i in range(9))
    hocheck = 0
    vcheck = 0
    scheck = 0
    realcheck = 0
    for i in range(9):
        horizon = []
        for j in range(9):
            if puzzle[i][j] not in horizon:
                horizon.append(puzzle[i][j])
            horizon.sort()
            if horizon == ['1','2','3','4','5','6','7','8','9']:
                hocheck += 1
    if hocheck == 9:
        realcheck += 1
    else:
        print('#{} {}'.format(tc, 0))

    for n in range(9):
        vertical = []
        for m in range(9):
            if puzzle[m][n] not in vertical:
                vertical.append(puzzle[m][n])
            vertical.sort()
            if vertical == ['1','2','3','4','5','6','7','8','9']:
                vcheck += 1
    if vcheck == 9:
        realcheck += 1
    else:
        print('#{} {}'.format(tc, 0))

    for k in range(0,9,3):
        square = []
        for l in range(0,9,3):
            for z in range(3):
                for x in range(3):
                    if puzzle[k+z][l+x] not in square:
                        square.append(puzzle[k+z][l+x])
            square.sort()
            if square == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                scheck += 1
    if scheck == 9:
        realcheck += 1
    else:
        print('#{} {}'.format(tc, 0))

    if realcheck == 3:
        print('#{} {}'.format(tc, 1))