import sys
sys.stdin = open("input.txt", "r")

T = 10

for t in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(n):
        arr.sort()
        if arr[-1] - arr[0] <= 1:
            break
        arr[0] += 1
        arr[-1] -= 1

    arr.sort()
    answer = arr[-1] - arr[0]

    print("#%d %d" % (t, answer))
