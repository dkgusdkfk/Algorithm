def search(board, r, c, card):
    if card != 0:
        for i in range(4):
            for j in range(4):
                if board[i][j] == card:
                    return (i, j, 0)
    else:


    return (r, c, card)

def solution(board, r, c):
    answer = 0
    b = [[0]*4]*4

    # dic = {}
    # for i in range(4):
    #     for j in range(4):
    #         if board[i][j] != 0:
    #             dic[board[i][j]] = (i,j)

    if board[r][c] != 0:
        card = board[r][c]
        board[r][c] = 0

    while(board!=b):
        r, c, card = search(board, r, c, card)
        board[r][c] = 0

    return answer


board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
print(solution(board, 1, 0))