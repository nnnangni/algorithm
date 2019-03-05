T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    list_num = list(map(int, input().split()))
    max_list = 0
    min_list = 0
    for i in range(M):
        min_list += list_num[i]
        max_list += list_num[i]

    for i in range(N-M+1):
        sum_list = 0
        for j in range(M):
            sum_list += list_num[i+j]
        if sum_list > max_list:
            max_list = sum_list
        if sum_list < min_list:
            min_list = sum_list

    print("#", end="")
    print(test_case, end=" ")
    print(max_list - min_list)