A = [1,2,3]
N = 3

for i in range(2**N):
    # i를 비트단위로 접근
    for j in range(N-1, -1, -1):
        # i의 j번비트검사한 결과가 0
        if i&(1<<j)!=0: # A[j]가 포함되면
            print(A[j], end='')
    print()

for i in range(2**N):
    s = 0
    for j in range(N):
        if i&(1<<j)!=0:
            s += A[j] #부분집합 원소의 합합
            print(A[j], end='')
    print(' ', end='')
    print(s)
    print()
