import sys
input = sys.stdin.readline

n = int(input())

p = []
for _ in range(n):
    age, name = input().split()
    p.append([int(age), name])

p.sort(key=lambda x: x[0])

for age, name in p:
    print(age, name)
