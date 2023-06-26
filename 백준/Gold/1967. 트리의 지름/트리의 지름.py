import sys

sys.setrecursionlimit(10 ** 6)  # 최대 재귀 깊이 변경
input = sys.stdin.readline

n = int(input())
arr = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])
    arr[b].append([a, c])


def dfs(s, d, v):
    global result, node
    flag = 0
    for i, j in arr[s]:
        if v[i]:
            continue
        v[i] = True
        dfs(i, d + j, v)
        flag = 1
    if flag == 0:
        if result < d:
            result = d
            node = s
        return


result = 0
node = 0
visited = [False] * (n + 1)
visited[1] = True
dfs(1, 0, visited)

visited = [False] * (n + 1)
visited[node] = True
result = 0
dfs(node, 0, visited)
print(result)