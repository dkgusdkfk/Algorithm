import sys
sys.stdin = open("input.txt", "r")


def dfs(idx, c):
    global answer
    if c == int(cnt):
        answer = max(int(''.join(data)), answer)
        return

    for i in range(idx, len(data)):
        for j in range(i+1, len(data)):
            if data[i] <= data[j]:
                data[i], data[j] = data[j], data[i]
                dfs(i, c+1)
                data[i], data[j] = data[j], data[i]

    if answer == 0 and c < int(cnt):
        if (int(cnt) - c) % 2 != 0:
            data[-1], data[-2] = data[-2], data[-1]
        dfs(idx, int(cnt))

T = int(input())

for t in range(1, T+1):
    data, cnt = input().split()
    data = list(data)
    answer = 0
    dfs(0, 0)
    print("#%d %d" % (t, answer))