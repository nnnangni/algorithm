T = int(input())

for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N+1):
        new = []
        for j in range(len(A)):
            if A[j] <= K:
                count += 1
                start = A[j]
                new.append(A[j])
                if len(new) >=2:
                    count -= 1
            # if start+K in A or start+K <= A[j]:
            #         count += 1
            #         start = start+K
    print(count)