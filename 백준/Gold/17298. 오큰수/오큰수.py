n = int(input())
arr = list(map(int, input().split()))
result = [-1 for _ in range(n)]

stack = [0]

for i in range(1, n):
    while stack and arr[stack[-1]] < arr[i]:
        result[stack.pop()] = arr[i]
    stack.append(i)

print(*result)