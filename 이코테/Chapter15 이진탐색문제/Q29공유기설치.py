import sys

n, c = map(int, sys.stdin.readline().split())

a = []
for _ in range(n):
    a.append(int(sys.stdin.readline()))

a.sort()

start = 1
end = a[-1] - a[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    count = 1
    value = a[0]
    for i in range(1, n):
        if a[i] >= value + mid:
            count += 1
            value = a[i]
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)