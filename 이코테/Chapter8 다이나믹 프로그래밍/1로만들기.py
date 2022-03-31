# 숫자 입력
N = int(input())

d = [0] * N

def cal(N):
    if N % 5 == 0:
        N /= 5
    elif N % 3 == 0:
        N /= 3
    elif N % 2 == 0:
        N /= 2
    else:
        N -= 1

    return N

count = 0
while N != 1:
    if cal(N-1) < cal(cal(N)):
        N = cal(N-1)
        count += 1
    else:
        N = cal(N)

    count += 1

print(count)