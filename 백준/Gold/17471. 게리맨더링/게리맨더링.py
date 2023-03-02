import sys

input = sys.stdin.readline


def subset(cnt):
    global isSelected
    if cnt == N:
        makeSet(N)
        for i in range(1, N + 1):
            if isSelected[i]:
                for j in range(len(arr[i])):
                    if isSelected[arr[i][j]]:
                        union(i, arr[i][j])
            else:
                for j in range(len(arr[i])):
                    if not isSelected[arr[i][j]]:
                        union(i, arr[i][j])
        check()
        return
    isSelected[cnt] = True
    subset(cnt + 1)
    isSelected[cnt] = False
    subset(cnt + 1)


def check():
    global result, parents
    s = set()
    for i in range(1, N + 1):
        s.add(findSet(i))

    if len(s) == 2:
        a = 0
        b = 0
        flag = parents[1]
        for i in range(1, N + 1):
            if parents[i] == flag:
                a += p[i - 1]
            else:
                b += p[i - 1]
        result = min(result, abs(a - b))


def makeSet(n):
    global parents
    for i in range(1, n + 1):
        parents[i] = i


def findSet(x):
    global parents
    if x == parents[x]:
        return x
    parents[x] = findSet(parents[x])
    return parents[x]


def union(a, b):
    global parents
    a = findSet(a)
    b = findSet(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


N = int(input())
p = list(map(int, input().split()))
isSelected = [False] * (N + 1)
parents = [0] * (N + 1)

arr = [[]]
for _ in range(N):
    arr.append(list(map(int, input().split()))[1:])

result = 1e9
subset(0)
print(result if result != 1e9 else -1)