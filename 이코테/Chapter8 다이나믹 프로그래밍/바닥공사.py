# N 입력
N = int(input())

# DP 테이블 초기화
d = [0] * 1001

d[1] = 1
d[2] = 3

for i in range(3, N+1):
    if i%2 != 0:
        d[i] = (d[i-1]*((i+1)//2) - (i//2)) % 796796
    else:
        d[i] = (d[i-2] * d[2]) % 796796

print(d[i])

'''
n = int(input())

d = [0] * 1001

d[1] = 1
d[2] = 3
for i in range(3, n+1):
    d[i] = (d[i-1] + 2 * d[i-2]) % 796796

print(d[n])
'''