# 강사님이 작성하신 코드

N = int(input())
h = list(map(int, input().split())) + [0] # 끝은 무조건 내리막으로 끝나도록
start = 0 # 오르막 구간의 시작 인덱스
status = 0 # 오르막 구간 1, 나머지는 0
maxV = 0 # 전체 오르막 구간에 대해 비교할 MAX
for i in range(N): # 오른쪽과 비교할 자리 i
    if status==0 and h[i]<h[i+1]:
        start = i # 오르막 시작
        status = 1
    elif status==1 and h[i]>=h[i+1]: # i에서 오르막이 끝나면
        diff = h[i]-h[start] # 오르막 구간의 높이 차이
        if maxV < diff: # 최대 오르막 찾기
            maxV = diff
        status = 0
print(maxV)

