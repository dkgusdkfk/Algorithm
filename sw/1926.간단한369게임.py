import sys
sys.stdin = open("input.txt", "r")

N = int(input())

answer = []
for n in range(1, N+1):
    arr = list(str(n))
    c = arr.count('3') + arr.count('6') + arr.count('9')
    if c == 0:
        answer.append(n)
    else:
        answer.append('-'*c)

print(*answer)
