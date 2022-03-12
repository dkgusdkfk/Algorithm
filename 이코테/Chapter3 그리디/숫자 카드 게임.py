#N, M 입력
N, M = map(int, input().split())

min_list = [] #각 행의 가장 작은 수를 넣을 리스트
for i in range(N):
    min_list.append(min(list(map(int, input().split())))) #각 행을 입력받아 각 행에서 가장 작은 수를 min_list에 append

result = max(min_list) # 각 행에서 가장 작은 수 중 가장 큰 수 선택

print(result) #결과 값 출력