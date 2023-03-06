n = 0
m = 0

def rotate(arr, g):
    m = len(arr)
    for _ in range(4):
        new_arr = [[0] * m for _ in range(m)]
        for r in range(m):
            for c in range(m):
                new_arr[c][m - r - 1] = arr[r][c]
        if match(new_arr, g):
            return True
        arr = new_arr
    return False

def match(arr, g):
    m = len(arr)
    l = len(g)
    for i in range(l-m+1):
        for j in range(l-m+1):
            new_g = [gr[:] for gr in g]
            for r in range(m):
                for c in range(m):
                    new_g[i+r][i+c] = arr[r][c]
            if check(new_g):
                return True
    return False

def check(array):
    global n, m
    for r in range(n):
        for c in range(n):
            if array[m + r - 1][m + c - 1] == 0:
                return False
    return True


def solution(key, lock):
    global n, m

    n = len(lock)
    m = len(key)
    l = n + 2*m - 2

    graph = [[0]*l for _ in range(l)]
    for i in range(n):
        for j in range(n):
            graph[m-1+i][m-1+j] = lock[i][j]

    answer = rotate(lock, graph)

    return answer