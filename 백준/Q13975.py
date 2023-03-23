from queue import PriorityQueue
import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    queue = PriorityQueue()
    list(map(lambda x: queue.put(int(x)), input().split()))

    result = 0
    while queue.qsize() > 1:
        x = queue.get()
        y = queue.get()
        result += x + y
        queue.put(x + y)

    print(result)
