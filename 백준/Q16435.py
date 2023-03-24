n, l = map(int, input().split())
fruits = sorted(list(map(int, input().split())))

for f in fruits:
    if l >= f:
        l += 1
print(l)