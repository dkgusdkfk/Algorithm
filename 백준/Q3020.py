import sys
input = sys.stdin.readline

n, h = map(int, input().split())

a = []
b = []
for i in range(n):
    if i % 2 == 0:
        a.append(int(input()))
    else:
        b.append(int(input()))
a.sort()
b.sort()

def check(arr, h):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] <= h:
            start = mid + 1
        else:
            end = mid - 1
    return len(arr) - (end + 1)

minCnt, cnt = n, 0
for height in range(1, h+1):
    count = check(a, height - 1) + check(b, h - height)

    if count < minCnt:
        minCnt = count
        cnt = 1
    elif count == minCnt:
        cnt += 1

print(minCnt, cnt)