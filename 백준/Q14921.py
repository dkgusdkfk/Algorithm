n = int(input())
arr = list(map(int, input().split()))

start, end = 0, n-1
result = 1e9
while start < end:
    temp = arr[start] + arr[end]
    if abs(temp) < abs(result):
        result = temp
    if temp > 0 :
        end -= 1
    else:
        start += 1
print(result)