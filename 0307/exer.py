N = int(input())
score = list(map(int, input().split()))
mode = {}
for i in score:
    if i in mode:
        mode[i] += 1
    else:
        mode[i] = 1

print(mode)
maxs = {}
for idx, val in mode.items():
    if val == max(mode.values()):
        maxs[idx] = val
print(maxs)
if len(maxs) == 1:
    print(maxs.values()[0])
else:
    print(max(maxs.keys()))
print("---")
