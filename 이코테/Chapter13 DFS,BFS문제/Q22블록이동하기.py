from collections import deque

def solution(board):
    answer = 0

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    n = len(board)
    x, y = 0, 1
    d = 0 # 가로

    queue = deque()
    queue.append((x,y,d))
    while queue:
        x, y, d = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if board[nx][ny] == 0:
                if d==0 and (i==0 or i==1):
                    if board[x+dx[i]][y-1]==0:
                        board[nx][ny] = board[x][y] + 1
                        queue.append((nx, ny, d))
                    else:
                        if board[x-dx[i]][y-1] == 0 and board[x-dx[i]][y] == 0:
                            d == 1
                            board[nx][ny] = board[x][y] + 2
                            queue.append((nx, ny, d))
                elif d==1 and (i==2 or i==3):
                    if board[x-1][y+dy[i]]==0:
                        board[nx][ny] = board[x][y] + 1
                        queue.append((nx, ny, d))
                    else:
                        if board[x-i][y-dy[i]] == 0 and board[x][y-dy[i]] == 0:
                            d == 0
                            board[nx][ny] = board[x][y] + 2
                            queue.append((nx, ny, d))
                else:
                    board[nx][ny] = board[x][y] + 1
                    queue.append((nx, ny, d))

    answer = board[n-1][n-1]

    return answer

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))