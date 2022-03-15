# 맵 크기 입력
N, M = map(int, input().split())

# 게임 캐릭터가 있는 칸의 좌표와 방향 입력
x, y, d = map(int, input().split())

# 방향 정의(북,동,남,서)
dir = [(0,-1), (1,0), (0,1), (-1,0)]

# 맵 입력
Map = []
for n in range(N):
    Map.append(list(map(int, input().split())))

c = 0   # 회전 수
Map[x][y] = -1  # 시작 땅 -1로 변경
while True:
    # 왼쪽으로 회전
    m_x = x + dir[d][0]
    m_y = y + dir[d][1]
    d = (4 + (d - 1)) % 4
    c += 1

    if Map[m_x][m_y] == 0:    # 가보지 않은 칸이 존재한다면 이동 후 칸 -1로 변경
        x = m_x
        y = m_y
        Map[x][y] = -1
        c = 0

    if c == 4:  # 네방향 모두 이미 가본 칸이거나 바다로 되어있는 칸인 경우 한칸 뒤로 이동
        x -= dir[(4 + (d + 1)) % 4][0]
        y -= dir[(4 + (d + 1)) % 4][1]
        c = 0

        if Map[x][y] == 1:   # 뒤쪽 방향이 바다인 칸인 경우 움직임 멈춤
            break

print(Map)

count = 0
for n in range(N):
    count += Map[n].count(-1)   # 방문한 칸 수 세기

print(count)    # 결과 출력