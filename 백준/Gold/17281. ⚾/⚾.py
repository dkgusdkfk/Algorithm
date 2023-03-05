from itertools import permutations
import sys

input = sys.stdin.readline


def checkScore(plist, inning):
    idx = 0
    score = 0
    for i in range(inning):
        out = 0
        b1, b2, b3 = 0, 0, 0
        while out < 3:
            if arr[i][plist[idx]] == 0:
                out += 1
            elif arr[i][plist[idx]] == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif arr[i][plist[idx]] == 2:
                score += b2 + b3
                b1, b2, b3 = 0, 1, b1
            elif arr[i][plist[idx]] == 3:
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            else:
                score += b1 + b2 + b3 + 1
                b1, b2, b3 = 0, 0, 0
            idx = (idx + 1) % 9

    return score


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

result = 0
for p in permutations(range(1, 9)):
    p = list(p)
    p.insert(3, 0)
    result = max(result, checkScore(p, n))

print(result)