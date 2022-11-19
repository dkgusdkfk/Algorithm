import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    result = 0

    n = int(input())

    s, e = n//2, n//2
    for i in range(n):
        result += sum(list(map(int, input()))[s:e+1])
        if i < n//2:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1

    print("#%d %d" % (t, result))