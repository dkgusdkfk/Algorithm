import sys

sys.setrecursionlimit(10 ** 6)  # 최대 재귀 깊이 변경
input = sys.stdin.readline

N = int(input())
arr = [[] for _ in range(N + 1)]  # 트리 간선 정보 저장
for _ in range(N - 1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


def dfs(s):
    visited[s] = True
    for next in arr[s]:
        if visited[next]:
            continue
        dfs(next)
    if not ea[s]:
        for next in arr[s]:
            ea[next] = True


ea = [False] * (N + 1)
visited = [False] * (N + 1)
visited[1] = True
dfs(1)

print(ea.count(True))