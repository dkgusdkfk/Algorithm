from collections import deque
R, C = map(int, input().split())

graph = []
queue = deque()
jihoon = (0, 0)
for r in range(R):
    g = []
    for c in range(C):
        g.append(input())
        if g[c] == 'J':
            jihoon = ('J', r, c)
        elif g[c] == 'F':
            queue.append(('F', r, c))
    graph.append(g)
queue.append(jihoon)

while queue:
    pass
