import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    result = 0

    s = input()

    for i in range(1,30):
        if s[i] == s[0]:
            if s[:i] == s[i:i*2]:
                result = i
                break

    print("#%d %d" % (t, result))

