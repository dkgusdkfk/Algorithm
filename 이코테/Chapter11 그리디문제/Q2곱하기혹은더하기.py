s = list(map(int, input()))

result = s[0]

for i in s[1:]:
    if result == 0 or i == 0:
        result += i
    else:
        result *= i

print(result)