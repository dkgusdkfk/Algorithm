import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    num = list(map(int, input().split()))

    result = round(sum(num)/len(num))

    print("#%d %d" % (t, result))
