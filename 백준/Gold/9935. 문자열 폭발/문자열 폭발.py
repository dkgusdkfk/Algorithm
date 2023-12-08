S = list(input())
s = list(input())
l = len(s)
temp = s[-1]

stack = []
for i in S:
    stack.append(i)
    if stack[-1] == temp and stack[-l:] == s:
        for j in range(l):
            stack.pop()

print(''.join(stack) if stack else 'FRULA')