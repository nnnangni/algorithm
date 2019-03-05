T = int(input())

for tc in range(1,T+1):
    P, A, B = map(int, input().split())
    def search(start,end,final):
        count = 0
        middle = 0
        while middle != final:
            middle = int((start + end) / 2)
            if final < middle:
               end = middle
            else:
                start = middle
            count += 1
        return count

    count_A = search(1,P,A)
    count_B = search(1,P,B)
    if count_A < count_B:
        print(f"#{tc} A")
    elif count_B < count_A:
        print(f"#{tc} B")
    else:
        print(f"#{tc} 0")