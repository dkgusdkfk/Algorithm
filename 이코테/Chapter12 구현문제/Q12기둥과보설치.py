def possible(answer):
    for x, y, a in answer:
        if a == 0:  # 기둥
            if y==0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer: # 바닥 위 or 보의 한쪽 끝부분 위 or 다른 기둥 위
                continue
            return False
        elif a == 1:    # 보
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):   # 한쪽 끝부분이 기둥 위 or 양쪽 끝부분이 다른 보와 동시 연결
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []

    for x, y, a, b in build_frame:
        if b == 0:
            answer.remove([x,y,a])
            if not possible(answer):
                answer.append([x,y,a])
        if b == 1:
            answer.append([x,y,a])
            if not possible(answer):
                answer.remove([x,y,a])

    return sorted(answer)

n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
print(solution(n, build_frame))