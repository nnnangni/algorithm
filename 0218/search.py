def search(arr, n, key):
    i = 0
    while i<n and arr[i]!=key:
        i += 1
    if i<n:
        return i
    else:
        return -1

def find(arr, n ,key):
    for i in range(n):
        if arr[i] == key:
            return i
    return -1

key = 4
A = [7,2,4]

print(search(A,3,4))
print(find(A,3,8))