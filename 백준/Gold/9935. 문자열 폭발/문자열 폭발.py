S = list(input())
s = list(input())
l = len(s)

stack = []
for i in S:
    stack.append(i)
    if stack[-l:] == s:
        for j in range(l):
            stack.pop()

print(''.join(stack) if stack else 'FRULA')