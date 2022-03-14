# 현재 나이트가 위치한 곳의 좌표 입력
n = input()

# 좌표 행렬로 구분
col = ord(n[0]) - ord('a') + 1
row = int(n[1])

count = 0

# 이동 가능한 방향
steps = [ (2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,2)]

# 이동가능한지 확인
for step in steps:
    m_col = col + step[1]
    m_row = row + step[0]
    if 1 <= m_col <= 8 and 1 <= m_row <= 8:
        count += 1

print(count)