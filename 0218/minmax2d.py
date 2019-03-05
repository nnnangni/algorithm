# # N * N 배열입력
# N = int(input())
# arr = [list(map(int, input().split())) for i in range(N)]
# print(arr)
# print(arr[1])
# print(arr[2][2])
#
# # 0으로 초기화된 5 * 5 배열만들기
# b = [[0] * 5 for i in range(5)]
# print(b)
# b[2][2] = 30
# print(b)
#
# # N*N 배열에서 최대, 최소 찾기
N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
#
# # 배열 요소 0<ai<100 인 조건
# maxV = 0
# minV = 100
# for i in range(N):
#     for j in range(N):
#         if(maxV<arr[i][j]):
#             maxV = arr[i][j]
#         if(minV>arr[i][j]):
#             minV = arr[i][j]
# print(maxV, minV)

maxI = 0
maxJ = 0
minI = 0
minJ = 0
# 최대값의 인덱스와 최대값
# 최소값의 인덱스와 최소값
for i in range(N):
    for j in range(N):
        if(arr[maxI][maxJ]<arr[i][j]):
        # 같은값이 있으면 행과 열이 작은 쪽을 출력
        # if(arr[maxI][maxJ]<=arr[i][j]):
            maxI = i
            maxJ = j
        if(arr[minI][minJ]>arr[i][j]):
            minI = i
            minJ = j
print(maxI, maxJ, arr[maxI][maxJ])
print(minI, minJ, arr[minI][minJ])