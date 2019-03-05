def f(n):
    if n>=2 and memo[n]==0:
        memo[n] = f(n-1) + f(n-2)
    return memo[n] # if문이 끝날때마다 memo리스트에 쌓아주는건지?

N = 10 # fibo 10 구하기
memo = [0]*(N+1) # 인덱스로 N만큼 있어야됨
memo[0] = 0
memo[1] = 1

print(f(N))
print(memo)

# 피보나치 DP적용
F = [0] * (N+1)
F[0] = 0
F[1] = 0
for n in range(2, N+1):
    F[n] = F[n-1] + F[n+2]
print(F)