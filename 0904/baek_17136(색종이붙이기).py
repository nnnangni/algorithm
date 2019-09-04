def re(n,cnt): # 사용한 종이수, s 남은 1 개수
    global minpaper, paper, arr
    if cnt==0:
        if minpaper>n:
            minpaper = n
    elif minpaper==4:
        return
    elif sum(paper)==0:
        return
    else:
        for i in range(10):
            for j in range(10):
                if arr[i][j]==1 and check[i][j]==0:
                    # 남은 종이 크기별로 덮어보기
                    plist = [0,1,2,3,4]
                    for p in plist:
                        psum = 0
                        for m in range(p):
                            for n in range(p):
                                if arr[i+m][j+n]==1 and check[i+m][j+n]==0:
                                    psum += 1
                        if psum==p*p:
                            re(n+1,cnt-p*p)


arr = [list(map(int,input().split())) for i in range(10)]
check = [[0]*10 for i in range(10)]
cnt = 0
for i in range(10):
    for j in range(10):
        if arr[i][j]==1:
            cnt += 1
minpaper = 26
paper = [5,5,5,5,5]

re(0,cnt)

if minpaper==26:
    minpaper = -1

print(minpaper)