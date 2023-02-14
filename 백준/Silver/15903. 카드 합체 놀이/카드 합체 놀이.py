from queue import PriorityQueue
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
queue = PriorityQueue()
list(map(lambda x: queue.put(int(x)), input().split()))

for _ in range(m):
    x = queue.get()
    y = queue.get()
    queue.put(x + y)
    queue.put(x + y)

result = 0
while not queue.empty():
    result += queue.get()
print(result)