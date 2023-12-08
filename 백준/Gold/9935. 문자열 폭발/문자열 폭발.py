S = list(input())
s = list(input())
l = len(s)

stack = S[:l]
if stack == s:
    stack = []
for i in S[l:]:
    stack.append(i)
    if stack[-l:] == s:
        for j in range(l):
            stack.pop()

if not stack:
    print("FRULA")
else:
    print(*stack, sep="")