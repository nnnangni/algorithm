# 길이가 3인 순열 생성
for i in range(1,4):
    for j in range(1,4):
        if i!=j:
            for k in range(1,4):
                if j!=k and i!=k:
                    print(i,j,k)