H, W = map(int, input().split())
arr = list(map(int, input().split()))
print(arr)
result = 0
for idx in range(1, W-1):
    minValue = min(max(arr[:idx]), max(arr[idx+1:]))
    if arr[idx] < minValue:
        result += minValue - arr[idx]
print(result)