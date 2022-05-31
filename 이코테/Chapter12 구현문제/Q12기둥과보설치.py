def solution(n, build_frame):
    answer = [[]]

    array = [[0]*n]*n   # 0:빈칸, 1:기둥, 2:보, 3:기둥+보, 5:기둥+보*2

    for b in build_frame:
        x, y = b[0], b[1]
        if b[3] == 1:   # 추가
            if b[2] == 0:   # 기둥
                if x+1 <= n:
                    if array[x][y] < 3:
                        array[x][y] = 1
                        array[x+1][y] = 1
            elif b[2] == 1: # 보
                if y+1 <= n:
                    if array[x][y] == 1:
                        array[x][y]




    return answer

n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
print(solution(n, build_frame))