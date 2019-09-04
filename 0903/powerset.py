# m개의 원소에서 1개 이상, 최대 M개를 고르는 방법
# 비트연산으로 부분집합만들기
arr = [6,1,9]
M = 3
c = 13
maximum = 0
for i in range(1,2**M-1): # 1에서 2^M-1까지 2진수 생성
    setsum = 0 # 부분집합의 합
    honeysum = 0
    # 비트
    for j in range(M): # 0,1,2번 비트
        # i에 대해서 j번 비트를 검사해서 1이면,(j번 비트가 나타내는 위치는 부분집합에 포함됨.)
        # 합계가 제한량 이하면,
        if i&(1<<j)!=0 and setsum+arr[j]<=c:
            # 검사하는 비트가 0이면 & 연산 결과가 0
            setsum += arr[j]
            honeysum += (arr[j])**2
    # 부분집합 1개를 생성할 때 마다 비교
    if maximum<honeysum:
        maximum = honeysum
# return maximum