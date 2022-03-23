# N 입력
N = int(input())

# 가게에 있는 전체 부품 입력
arrayN = list(map(int, input().split()))

# M 입력
M = int(input())

# 확인요청한 부품 번호
arrayM = list(map(int, input().split()))

# 정렬
arrayN.sort()

# 이진트리 탐색
def search(a, b, array, m):
    c = (a+b)//2

    if a == c:
        return 0

    if m == array[c]:
        return 1
    elif m < array[c]:
        b = c
    else:
        a = c

    if search(a, b, array, m) == 0:
        return 0
    else:
        return 1

# 결과 출력
for m in range(M):
    a = 0
    b = N - 1
    result = search(a, b, arrayN, arrayM[m])
    print(result)
    if result == 0:
        print('no', end=' ')
    else:
        print('yes', end=' ')