T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    maximum = A[0]
    minimum = A[0]
    for i in range(1, len(A)):
        if maximum < A[i]:
            maximum = A[i]
        if minimum > A[i]:
            minimum = A[i]
    print(f"#{test_case} {maximum-minimum}")



