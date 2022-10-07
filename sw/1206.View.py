import sys
sys.stdin = open("input.txt", "r")

# T = int(input())
T = 10

for t in range(1, T+1):
    n = int(input())
    array = list(map(int, input().split()))
    answer = 0
    for i in range(2, n-2):
        a = array[i] - max(array[i-2:i] + array[i+1:i+3])
        answer += a if a > 0 else 0

    print("#%d %d" % (t, answer))
