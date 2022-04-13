s = map(int, input())

num = []
for i in s:
    num.append(int(i))

result = num[0]

for i in num[1:]:
    if result == 0 or i == 0:
        result += i
    else:
        result *= i

print(result)