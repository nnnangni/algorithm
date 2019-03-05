for tc in range(1,11):
    N=int(input())
    arr = [list(map(int, input().split())) for i in range(100)]

    dsum1=0
    dsum2=0
    sumList=[]

    for i in range(100):
        dsum1 += arr[i][i]
        dsum2 += arr[i][99-i]

        rsum = 0
        csum = 0

        for j in range(100):
            rsum+=arr[i][j]
            csum+=arr[j][i]
        sumList.append(rsum)
        sumList.append(csum)
    sumList.append(dsum1)
    sumList.append(dsum2)

    res=0
    for k in sumList:
        if (res< k):
            res = k

    print(f"#{tc} {res}")