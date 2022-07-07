t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    array = [[0 for _ in range(m)] for _ in range(n)]
    a = list(map(int, input().split()))
    gold = []
    for i in range(n):
        gold.append(a[i*m:i*m+m])

    for i in range(n):
        array[i][0] = gold[i][0]

    for i in range(1,m):
        for j in range(n):
            value = []
            for k in [-1, 0, 1]:
                if 0 <= j+k < n:
                    value.append(array[j+k][i-1])
            array[j][i] = max(value) + gold[j][i]

    result = max(array, key=lambda x:x[-1])[-1]
    print(result)
