import sys

n = int(sys.stdin.readline())

value = [[0 for _ in range(i)] for i in range(1, n+1)]

array = []
for _ in range(n):
    array.append(list(map(int, sys.stdin.readline().split())))

value[0][0] = array[0][0]

for i in range(1,n):
    value[i][0] = value[i-1][0] + array[i][0]
    for j in range(1, i):
        value[i][j] = max(value[i-1][j], value[i-1][j-1]) + array[i][j]
    value[i][-1] = value[i-1][-1] + array[i][-1]

print(max(value[-1]))