n = int(input())
num = sorted(list(map(int, input().split())))

total = 0
temp = 0
for n in num:
    total += temp + n
    temp += n
print(total)