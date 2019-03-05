

for n in range(1,11):
    N = int(input())
    b = list(map(int, input().split()))
    count = 0
    for idx, val in enumerate(b):
        if idx > 1 and idx < N-2:
            maximum = max(b[idx-2], b[idx-1], b[idx+1], b[idx+2])
            if b[idx] > maximum:
                view = b[idx]-maximum
                count += view

    print('#', end='')
    print(n, end=' ')
    print(count)