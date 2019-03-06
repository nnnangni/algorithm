import sys
sys.stdin = open('1970input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    new = N
    count50000 = 0
    count10000 = 0
    count5000 = 0
    count1000 = 0
    count500 = 0
    count100 = 0
    count50 = 0
    count10 = 0
    while new>9:
        if new>=50000:
            new = new-50000
            count50000 += 1
        if new>=10000 and new<50000:
            new = new-10000
            count10000 += 1
        if new>=5000 and new<10000:
            new = new-5000
            count5000 += 1
        if new>=1000 and new<5000:
            new = new-1000
            count1000 += 1
        if new>=500 and new<1000:
            new = new-500
            count500 += 1
        if new>=100 and new<500:
            new = new-100
            count100 += 1
        if new>=50 and new<100:
            new = new-50
            count50 += 1
        if new>=10 and new<50:
            new = new-10
            count10 += 1
    print('#{}'.format(tc))
    print(count50000, count10000, count5000, count1000, count500, count100, count50, count10)


