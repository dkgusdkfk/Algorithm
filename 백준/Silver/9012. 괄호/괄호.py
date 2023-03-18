from collections import deque
import sys
input = sys.stdin.readline


def check(str):
    stack = deque()
    for s in str:
        if s == '(':
            stack.append(s)
        else:
            if not stack:
                return "NO"
            if stack.pop() != '(':
                return "NO"
    if stack:
        return "NO"
    return "YES"


n = int(input())
for _ in range(n):
    print(check(input().strip()))