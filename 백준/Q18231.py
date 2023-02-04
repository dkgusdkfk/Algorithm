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

yes = []
no = []
for c in kList:
    flag = 0
    for r in road[c]:
        if r not in kList:
            no.append(c)
            flag = 1
            break
    if flag == 0:
        yes.append(c)
print(yes, no)

if len(yes) + len(no) == n:
    print(yes)
else:
    print(-1)