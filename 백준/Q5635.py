n = int(input())

info = []
for _ in range(n):
    name, day, month, year = input().split();
    info.append([int(year), int(month), int(day), name])

info.sort()
print(info[-1][-1])
print(info[0][-1])
