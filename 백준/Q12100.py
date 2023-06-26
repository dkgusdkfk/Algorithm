from copy import deepcopy

n = int(input())

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

def up(b):
    for i in range(n):
        p = 0
        for j in range(1, n):
            if b[j][i]:
                temp = b[j][i]
                b[j][i] = 0

                if b[p][i] == 0:
                    b[p][i] = temp
                elif b[p][i] == temp:
                    b[p][i] *= 2
                    p += 1
                else:
                    p += 1
                    b[p][i] = temp

    return b

def down(b):
    for i in range(n-1, -1, -1):
        p = n-1
        for j in range(n-2, -1, -1):
            if b[j][i]:
                temp = b[j][i]
                b[j][i] = 0

                if b[p][i] == 0:
                    b[p][i] = temp
                elif b[p][i] == temp:
                    b[p][i] *= 2
                    p -= 1
                else:
                    p -= 1
                    b[p][i] = temp

    return b

def left(b):
    for j in range(n):
        p = 0
        for i in range(1, n):
            if b[j][i]:
                temp = b[j][i]
                b[j][i] = 0

                if b[j][p] == 0:
                    b[j][p] = temp
                elif b[j][p] == temp:
                    b[j][p] *= 2
                    p += 1
                else:
                    p += 1
                    b[j][p] = temp

    return b

def right(b):
    for j in range(n-1, -1, -1):
        p = n-1
        for i in range(n-2, -1, -1):
            if b[j][i]:
                temp = b[j][i]
                b[j][i] = 0

                if b[j][p] == 0:
                    b[j][p] = temp
                elif b[j][p] == temp:
                    b[j][p] *= 2
                    p -= 1
                else:
                    p -= 1
                    b[j][p] = temp

    return b

def dfs(k, board):
    global answer
    if k == 5:
        answer = max(answer, max(map(max, board)))
        return

    dfs(k+1, up(deepcopy(board)))
    dfs(k+1, down(deepcopy(board)))
    dfs(k+1, left(deepcopy(board)))
    dfs(k+1, right(deepcopy(board)))

answer = 0
dfs(0, board)
print(answer)
