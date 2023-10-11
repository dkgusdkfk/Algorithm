g, s = map(int, input().split())
W = input()
S = input()

a = [0 for _ in range(ord('z'))]
b = [0 for _ in range(ord('z'))]

for i in range(g):
    a[ord(W[i]) - 65] += 1
    b[ord(S[i]) - 65] += 1

count = 0
if a == b:
    count += 1
for i in range(s-g):
    b[ord(S[i]) - 65] -= 1
    b[ord(S[i+g]) - 65] += 1
    if a == b:
        count += 1
print(count)