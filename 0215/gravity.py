import sys
# 표준입력을 바꿔놓는 것
sys.stdin = open('input.txt', 'r')

arr = list(map(int, input().split()))
for i in range(len(arr)):
    print(arr[i], end=' ')