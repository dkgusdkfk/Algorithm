n = int(input())
arr = list(map(int, input().split()))
p = [0] * n

for idx, k in enumerate(arr):
    c = 0
    for i in range(n):
        if p[i] == 0:
            if c == k:
                p[i] = idx + 1
                break
            c += 1
print(*p)