from heapq import heappush, heappop

n = int(input())
heap = []
for _ in range(n):
    heappush(heap, int(input()))

result = 0
while len(heap) > 1:
    k = heappop(heap) + heappop(heap)
    result += k
    heappush(heap, k)
print(result)
