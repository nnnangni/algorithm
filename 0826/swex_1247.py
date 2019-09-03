T = int(input())

def per(n,k,cx,cy,hx,hy):
    global cusorder, used, result, customerx, customery
    global mindistance
    if n==k:
        nx,ny = cx,cy
        dist = 0
        for m in range(N):
            dist += (abs(customerx[result[m]-1]-nx))
            nx = customerx[result[m]-1]
            dist += (abs(customery[result[m]-1]-ny))
            ny = customery[result[m]-1]
        dist += (abs(nx-hx)+abs(ny-hy))
        mindistance.append(dist)
    else:
        for i in range(k):
            if used[i]==0:
                used[i]=1
                result[n]=cusorder[i]
                per(n+1,k,cx,cy,hx,hy)
                used[i]=0

for i in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
    customerx = []
    customery = []
    cusorder = [i for i in range(1,N+1)]
    used = [0]*N
    result = [0]*N
    cx,cy,hx,hy = arr[0],arr[1],arr[2],arr[3]
    mindistance = []
    for j in range(4,2*N+4,2):
        customerx.append(arr[j])
        customery.append(arr[j+1])
    per(0,N,cx,cy,hx,hy)
    best = min(mindistance)
    print(f"#{i+1} {best}")


