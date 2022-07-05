# 보드크기 N
n = int(input())
# 사과 개수 K
k = int(input())
# 사과 위치
apple = []
for _ in range(k):
    apple.append(list(map(int, input().split())))
# 방향 변환 횟수 L
l = int(input())
# 방향 변환 정보
info = []
for _ in range(l):
    info.append(list(input().split()))

dir = {0:[0,1], 1:[1,0], 2:[0,-1], 3:[-1,0]}  #동,남,서,북 순서
# dx,dy랑 메모리 비교
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
snake = [[1,1]]
head = [1,1]
d = 0
time = 0

while(True):
    time += 1

    head[0] += dir[d][0]
    head[1] += dir[d][1]
    # head[0] += dx[d]
    # head[1] += dy[d]
    if not(1 <= head[0] <= n and 1 <= head[1] <= n) or head in snake:
        break

    snake.append(head[:])
    if head in apple:
        apple.remove(head)
    else:
        del snake[0]    # pop으로 변경 --> del은 반환하지 않기 때문에 del이 더 빠름

    if info != []:
        if time == int(info[0][0]):
            if info[0][1] == 'L':
                d = (d - 1 + 4)%4
            elif info[0][1] == 'D':
                d = (d + 1)%4
            del info[0]

print(t)