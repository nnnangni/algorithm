def subset(bit):
    for i in range(4):
        if bit[i]==1:
            print(A[i], end=' ')
    print()

A = [1,2,3,4]
bit = [0,0,0,0]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                subset(bit)
