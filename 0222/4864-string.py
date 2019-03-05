T = int(input())
for tc in range(1,T+1):
    str1 = input()
    str2 = input()
    result = 0
    for i in range(len(str2)-len(str1)+1):
        if str1 == str2[i:i+len(str1)]:
            result = 1
