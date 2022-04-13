s = list(map(int, input()))

count = 0
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        count += 1

result = count // 2
print(result)
