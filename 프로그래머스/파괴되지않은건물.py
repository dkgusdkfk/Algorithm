def solution(board, skill):
    answer = 0

    m = len(board)
    n = len(board[0])

    array = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for type, r1, c1, r2, c2, degree in skill:
        array[r1][c1] += degree if type == 2 else -degree
        array[r1][c2 + 1] += -degree if type == 2 else degree
        array[r2 + 1][c1] += -degree if type == 2 else degree
        array[r2 + 1][c2 + 1] += degree if type == 2 else -degree

    for i in range(m):
        for j in range(n):
            array[i][j+1] += array[i][j]

    for j in range(n):
        for i in range(m):
            array[i+1][j] += array[i][j]

    for i in range(m):
        for j in range(n):
            board[i][j] += array[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer

board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
print(solution(board, skill))