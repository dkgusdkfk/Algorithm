import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    total = sum([i for i in list(map(int, input().split())) if i%2])
    print("#%d %d" % (t, total))
