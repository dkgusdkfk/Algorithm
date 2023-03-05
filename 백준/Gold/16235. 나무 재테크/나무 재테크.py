from collections import deque
import sys

input = sys.stdin.readline

N, M, K = map(int, input().split(" "))
ground = [[5] * N for _ in range(N)]
A = [list(map(int, input().split(" "))) for _ in range(N)]
tree = [[deque() for _ in range(N)] for _ in range(N)]
for _ in range(M):
    X, Y, Z = map(int, input().split(" "))
    tree[X-1][Y-1].append(Z)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def spring_summer():
    for i in range(N):
        for j in range(N):
            newTree = deque()
            k = 0
            while tree[i][j]:
                z = tree[i][j].popleft()
                if ground[i][j] < z:
                    k += z // 2
                    continue
                ground[i][j] -= z
                newTree.append(z + 1)
            tree[i][j] = newTree
            ground[i][j] += k


def autumn_winter():
    for i in range(N):
        for j in range(N):
            for idx in range(len(tree[i][j])):
                z = tree[i][j][idx]
                if z % 5 == 0:
                    for d in range(8):
                        mx = i + dx[d]
                        my = j + dy[d]
                        if 0 <= mx < N and 0 <= my < N:
                            tree[mx][my].appendleft(1)
            ground[i][j] += A[i][j]


for _ in range(K):
    spring_summer()
    autumn_winter()

result = 0
for i in range(N):
    for j in range(N):
        result += len(tree[i][j])
print(result)