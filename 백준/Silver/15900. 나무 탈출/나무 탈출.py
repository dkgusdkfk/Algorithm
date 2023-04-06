import sys
sys.setrecursionlimit(10**6)    # 최대 재귀 깊이 변경
input = sys.stdin.readline

N = int(input())
arr = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


def dfs(s, d, v):
    global result
    flag = 0
    for i in arr[s]:
        if v[i]:
            continue
        v[i] = True
        dfs(i, d + 1, v)
        flag = 1
    if flag == 0:
        result += d


result = 0
visited = [False] * (N + 1)
visited[1] = True
dfs(1, 0, visited)

print("No" if result % 2 == 0 else "Yes")