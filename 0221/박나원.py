import sys
sys.stdin = open('input.txt','r')


for tc in range(1,11):
    tn = int(input())
    ladder = [list(map(int, input().split())) for i in range(100)]
    y = 98
    start = ladder[99].index(2)

    dir = "middle"
    while y > 0:
        if start>=1 and ladder[y][start-1]==1 and dir!="right":
            start -= 1
            dir = "left"
        elif start<=98 and ladder[y][start+1]==1 and dir!="left":
            start += 1
            dir = "right"
        else:
            y -= 1
            dir = "middle"


