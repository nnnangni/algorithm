# {1,2,3,4,5,6,7,8,9} 의 powerset 중 원소의 합이 10인 부분집합을 구하시오.

def f(n, k, m):
    global cnt
    if n==k: # 한개의 부분집합 완성
        s = 0
        for i in range(k): # 부분집합의 합 계산
            if b[i]==1:
                s += a[i]
        if s==m: # 문제에 주어진 합과 같으면 부분집합 출력
            cnt += 1
            for i in range(k):  # 부분집합의 합 계산
                if b[i] == 1:
                    print(a[i], end=' ')
            print()
        return

    else:
        b[n] = 0
        f(n+1, k, m)
        b[n] = 1
        f(n+1, k, m)


K = 10
M = 10 # 부분집합의 합
a = [1,2,3,4,5,6,7,8,9,10]
b = [0]*K
cnt = 0
f(0, K, M)
print(cnt)