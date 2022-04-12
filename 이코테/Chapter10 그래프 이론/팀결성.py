n, m = map(int, input().split())

array = [0] * (n + 1)
for i in range(n + 1):
    array[i] = i

for i in range(m):
    k, a, b = map(int, input().split())

    if k == 0:
        array[b] = array[a]
    else:
        if array[a] == array[b]:
            print('YES')
        else:
            print('NO')