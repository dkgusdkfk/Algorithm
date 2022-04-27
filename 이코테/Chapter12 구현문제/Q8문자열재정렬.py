s = input()

word = ""
sum = 0
for i in range(len(s)):
    if '0' <= s[i] <= '9':
        sum += int(s[i])
    else:
        word += s[i]

word = "".join(sorted(word))
word += str(sum)
print(word)