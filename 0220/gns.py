T = int(input())
for tc in range(1, T+1):
    test, N = input().split()
    old = {"ZRO":0, "ONE":1,"TWO":2, "THR":3, "FOR":4,
            "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
    arr = list(input().split())
    gns = []
    for i in arr:
        gns.append(old[i])
    gns.sort()
    new = {0:"ZRO", 1:"ONE", 2:"TWO", 3:"THR", 4:"FOR",
           5:"FIV", 6:"SIX", 7:"SVN", 8:"EGT", 9:"NIN"}
    print(f"#{tc}")
    for i in gns:
        print(new[i], end=" ")
    print()