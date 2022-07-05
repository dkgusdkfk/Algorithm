# 집의 수 n
n = int(input())

# 집 위치
array = list(map(int, input().split()))

array.sort()

result = array[(n-1)//2]    # n//2 - 1 ? --> 홀짝

print(result)