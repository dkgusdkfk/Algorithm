n = int(input())

xArray = list(map(int, input().split()))

xArray.sort()

group = 0
while xArray:
    for i in range(max(xArray)):
        xArray.pop()
    group += 1

print(group)
