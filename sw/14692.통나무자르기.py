import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    n = int(input())

    winner = 'Alice' if n % 2 == 0 else 'Bob'

    print("#%d %s" % (t, winner))
