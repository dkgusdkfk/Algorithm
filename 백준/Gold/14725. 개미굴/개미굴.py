import sys
input = sys.stdin.readline

n = int(input())
array = []
for _ in range(n):
    k, *a = input().split()
    array.append(a)
array.sort()

check = []
for arr in array:
    for i, a in enumerate(arr):
        if arr[:i+1] in check:
            continue
        print("--"*i + a)
        check.append(arr[:i+1])