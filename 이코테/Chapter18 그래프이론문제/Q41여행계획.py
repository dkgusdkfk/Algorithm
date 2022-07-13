import sys

n, m = int(input().split)

graph = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

