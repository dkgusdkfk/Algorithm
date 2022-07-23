import sys

test = int(input())

for _ in range(test):
    n = int(input())
    t = list(map(int, sys.stdin.readline().split()))
    m = int(input())
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())


