import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    n, m = map(int, input().split())

    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    answer = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            a = 0
            for k in range(m):
                a += sum(arr[i+k][j:j+m])
            if a > answer:
                answer = a

    print("#%d %d" % (t, answer))
