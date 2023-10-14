import sys
input = sys.stdin.readline

def depth(n, nodes):
    n = nodes[n]
    count = 0
    while n != 0:
        count += 1
        n = nodes[n]
    return count

def up(n, c, nodes):
    for _ in range(c):
        n = nodes[n]
    return n

t = int(input())
for _ in range(t):
    n = int(input())
    nodes = [0 for _ in range(n+1)]
    for _ in range(1, n):
        a, b = map(int, input().split())
        nodes[b] = a
    n1, n2 = map(int, input().split())
    d1 = depth(n1, nodes)
    d2 = depth(n2, nodes)

    if d1 > d2:
        n1 = up(n1, d1-d2, nodes)
    else:
        n2 = up(n2, d2-d1, nodes)

    while n1 != n2:
        n1 = nodes[n1]
        n2 = nodes[n2]
    print(n1)