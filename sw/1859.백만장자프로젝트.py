import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    n = int(input())
    array = list(map(int, input().split()))
    total = 0
    max_value = array[-1]
    for i in range(n-2, -1, -1):
        if max_value > array[i]:
            total += max_value - array[i]
        else:
            max_value = array[i]

    print("#%d %d" % (t, total))