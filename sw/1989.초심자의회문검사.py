import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    result = 1

    s = input()

    for i in range(len(s)//2):
        if s[i] != s[-1-i]:
            result = 0
            break

    print("#%d %d" % (t, result))