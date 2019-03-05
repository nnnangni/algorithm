M, N = map(int, input().split())
apt = [list(input()) for n in range(5*M+1)]
count0 = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
for i in range(1, M+1):
    for k in range(1, 5*N, 5):
        blind = []
        for j in range(5 * i - 4, 5 * i):
            if apt[j][k] == "*":
                blind.append("*")
        if len(blind) == 0:
            count0 += 1
        elif len(blind) == 1:
            count1 += 1
        elif len(blind) == 2:
            count2 += 1
        elif len(blind) == 3:
            count3 += 1
        else:
            count4 += 1
print(count0, count1, count2, count3, count4)