import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

arr = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])
    arr[b].append([a, c])


def dfs(s, d, v):
    global result
    flag = 0
    for i, j in arr[s]:
        if v[i]:
            continue
        v[i] = True
        dfs(i, d + j, v)
        flag = 1
    if flag == 0:
        result = max(result, d)


result = 0
visited = [False] * (N + 1)
visited[1] = True
dfs(1, 0, visited)
print(result)