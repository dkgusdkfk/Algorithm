# 얼음 틀의 길이 입력
N, M = map(int, input().split())

# 얼음 틀의 형태 입력
ice = []
for n in range(N):
    ice.append(list(map(int, input())))

def dfs(x, y):
    if not(0 <= x < N and 0 <= y < M):  # 좌표가 범위를 벗어나면 0 반환
        return 0
    if ice[x][y] == 0:  # 아직 방문하지 않았다면
        ice[x][y] = 1   # 방문처리
        # 상,하,좌,우 재귀적으로 호출
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return 1
    return 0

# 모든 위치에 음료수 채우기
count = 0
for n in range(N):
    for m in range(M):
        if dfs(n, m) == 1:
            count += 1

print(count)    # 결과 출력