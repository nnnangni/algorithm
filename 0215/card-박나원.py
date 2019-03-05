T = int(input())

for test_case in range(1, T + 1):
    N = list(map(int, input().split()))
    A = list(map(int, input()))

    cards = {}
    for i in A:
        if i in cards:
            cards[i] += 1
        else:
            cards[i] = 1

    max_key = 0
    max_val = 0
    for key in cards.keys():
        if cards[key] > max_val:
            max_val = cards[key]
            max_key = key
        if cards[key] == max_val:
            if key > max_key:
                max_key = key

    print(f"#{test_case} {max_key} {max_val}")