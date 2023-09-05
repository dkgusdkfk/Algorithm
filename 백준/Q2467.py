n = int(input())
arr = list(map(int, input().split()))
start, end = 0, n-1

x, y = arr[start], arr[end]
total = arr[start] + arr[end]

while start < end:
    if abs(total) > abs(arr[start] + arr[end]):
        x, y = arr[start], arr[end]
        total = arr[start] + arr[end]
    if arr[start] + arr[end] > 0:
        end -= 1
    else:
        start += 1

print(x, y)