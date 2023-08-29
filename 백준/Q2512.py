n = int(input())
arr = list(map(int, input().split()))
m = int(input())
start, end = 0, max(arr)

while start <= end:
    mid = (start + end) // 2

    sum = 0
    for a in arr:
        if a <= mid:
            sum += a
        else:
            sum += mid
    if sum <= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)