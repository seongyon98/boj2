import sys
input = sys.stdin.readline

def next_p(arr):
    n = len(arr)
    i = n - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1

    if i == 0:
        return False

    j = n - 1
    while arr[i - 1] >= arr[j]:
        j -= 1

    arr[i - 1], arr[j] = arr[j], arr[i - 1]
    arr[i:] = reversed(arr[i:])
    return True

n = int(input())
arr = list(map(int, input().split()))

if next_p(arr):
    print(' '.join(map(str, arr)))
else:
    print(-1)
