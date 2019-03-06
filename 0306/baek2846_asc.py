T = int(input())
N = list(map(int,input().split()))
i = 0
diff = []
asc = []
while i<len(N)-1:
    if N[i]< N[i+1]:
        asc.append(N[i])
        start = min(asc)
        end = N[i+1]
        diff.append(end-start)
        i += 1
    elif N[i]>=N[i+1]:
        diff.append(0)
        i += 1
        asc = []
print(max(diff))


