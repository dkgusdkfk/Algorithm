import sys
input = sys.stdin.readline

# N: 마을의 개수, M: 벽의 개수, K: 돌의 개수
N, M, K = map(int, input().split())
# 모래성의 개수 배열
sand = list(map(int, input().split()))
# 돌 위치 배열
rock = list(map(int, input().split()))
# rock = list(map(lambda x: [sand[int(x)-1], x], input().split()))

arr = []
for idx in range(K-1):
    arr.append([sum(sand[rock[idx]-1:rock[idx+1]-1]), rock[idx]])
arr.append([sum(sand[rock[-1]-1:]), rock[-1]])

arr.sort(reverse=True)
result = sorted(list(map(lambda x: x[1], arr[:M])))
print(*result, sep="\n")