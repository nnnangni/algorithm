import sys
sys.stdin = open('1948input.txt','r')

T = int(input())

day = [0,31,28,31,30,31,30,31,31,30,31,30,31]

for tc in range(1,T+1):
    m1, d1, m2, d2 = map(int, input().split())
    if m1 == m2:
        diff = d2-d1+1
    elif m2-m1==1:
        diff = day[m1]-d1+d2
    else:
        days = 0
        for i in range(m1+1,m2):
            days += day[i]
        diff = day[m1]-d1+days+d2+1
    print('#{} {}'.format(tc, diff))