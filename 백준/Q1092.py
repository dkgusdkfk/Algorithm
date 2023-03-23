n = int(input())
s = sorted(list(map(int, input().split())))
m = int(input())
boxes = sorted(list(map(int, input().split())))
idx = [[0] * n]
i = n-1
for j in range(m-1, -1, -1):
    if boxes[j] <= s[i]:
        idx[i] = j
        i -= 1
while idx[n-1] != -1:
    for i in range(n):
