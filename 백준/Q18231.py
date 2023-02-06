import sys
input = sys.stdin.readline

n, m = map(int, input().split())

road = {}
for i in range(1, n+1):
    road[i] = []

for _ in range(m):
    u, x = map(int, input().split())
    road[u].append(x)
    road[x].append(u)

k = int(input())
kList = list(map(int, input().split()))

check = [False] * (n+1)
answer = [True if i in kList else False for i in range(n+1)]
result = []

for i in kList:
    flag = 0
    for j in road[i]:
        if j not in kList:
            flag = 1
            break
    if flag == 0:
        result.append(i)
        check[i] = True
        for j in road[i]:
            check[j] = True
    if check == answer:
        print(len(result))
        print(*result)
        exit(0)
print(-1)
