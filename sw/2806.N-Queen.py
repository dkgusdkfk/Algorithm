import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def solution(arr, c):
    global n, result
    if c == n:
        result += 1
        return
    temp = [0] * n
    for i in range(len(arr)):
        # 열
        temp[arr[i]] = 1
        # 왼쪽 대각선
        if arr[i] - (c - i) >= 0:
            temp[arr[i] - (c-i)] = 1
        # 오른쪽 대각선
        if arr[i] + (c - i) < n:
            temp[arr[i] + (c-i)] = 1

    for i in range(n):
        if temp[i] == 0:
            solution(arr + [i], c + 1)


for t in range(1, T+1):
    n = int(input())
    result = 0
    solution([], 0)

    print('#%d %d' % (t, result))
