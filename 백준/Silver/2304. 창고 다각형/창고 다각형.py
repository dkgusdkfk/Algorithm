n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x: x[1])

start = min(arr)[0]
end = max(arr)[0]

result = 0

s = e = arr.pop()
result += s[1]
while s[0] != start or e[0] != end:
    k = arr.pop()
    if k[0] > e[0]:
        result += (k[0] - e[0]) * k[1]
        e = k
    elif k[0] < s[0]:
        result += (s[0] - k[0]) * k[1]
        s = k

print(result)