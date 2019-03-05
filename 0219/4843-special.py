T = int(input())
for tc in range(1,T+1):
    N = int(input())
    a = list(map(int,input().split()))
    for i in range(N-1,0,-1):
        for j in range(0,i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    # print(a)
    print(f"#{tc}")
    for i in range(5):
        print(a[len(a) - 1 - i], end=" ")
        print(a[i],end=" ")
    print()

