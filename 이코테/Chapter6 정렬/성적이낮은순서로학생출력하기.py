# 학생의 수 N 입력
N = int(input())

# 학생 이름, 성적 입력
array = []
for n in range(N):
    name, score = input().split()
    array.append((name,score))

# 정렬 기준
def setting(data):
    return data[1]

# 정렬
result = sorted(array, key = setting)

# 결과출력
for n in range(N):
    print(result[n][0], end=' ')