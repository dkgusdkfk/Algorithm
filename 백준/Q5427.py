from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def init():
    global R, C
    global graph, fire, position, visited

    C, R = map(int, input().split())

    graph = []
    fire = deque()
    position = deque()
    for r in range(R):
        g = list(input())
        for c in range(C):
            if g[c] == '@':
                position.append((r, c))
                g[c] = '.'
            elif g[c] == '*':
                fire.append((r, c))
        graph.append(g)
    visited = [[False for _ in range(C)] for _ in range(R)]

def spread():
    fSize = len(fire)
    while fSize > 0:
        x, y = fire.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if graph[nx][ny] == '.':
                    graph[nx][ny] = '*'
                    fire.append((nx, ny))
        fSize -= 1

def solution():
    t = 0
    while position:
        t += 1
        spread()
        pSize = len(position)
        while pSize > 0:
            x, y = position.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < R and 0 <= ny < C:
                    if graph[nx][ny] == '.' and not visited[nx][ny]:
                        position.append((nx, ny))
                        visited[nx][ny] = True
                else:
                    print(t)
                    return
            pSize -= 1
    print("IMPOSSIBLE")

def main():
    T = int(input())
    for _ in range(T):
        init()
        solution()

main()