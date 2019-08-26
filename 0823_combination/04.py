# 호출 횟수가 변하는 재귀 호출
# 1. 사용할 숫자를 배열에 저장한다.
# 2. 사용된 숫자의 위치를 표시할 배열 used를 준비한다.
# 3. 첫째 자리 결정 : 왼쪽부터 사용하지 않은 숫자를 찾으면 표시하고, 숫자를 복사한다.
# 4. 둘째 자리 결정 : 다음 자리를 정하기 위해 재귀호출을 한다.
# 5. 셋째 자리 결정
# 6. 세 개의 숫자를 골랐으므로 출력(하나가 완성됨)
# 7. 이전 단계로 돌아간다. used의 마지막 인덱스를 가리키고 있음.
# 8. 선택했던 숫자는 취소한다. 남은 숫자가 없으면 이전 단계로 간다.
# 9. 선택했던 숫자는 취소한다. 오른쪽에 남은 숫자가 있으면 선택한다.
K,M = 5,3
used=[0]*K
list=[i for i in range(1,K+1)]
result=[0]*M
def f(n,k,m):
    if n==m:
        # print(result)
        return
    else:
        for i in range(k):
            if used[i]==0:
                used[i]=1
                result[n]=list[i]
                print(result)
                f(n+1,k,m)
                used[i]=0
                print(used)
f(0,K,M)
