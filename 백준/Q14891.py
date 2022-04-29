def right(nArray):
    temp = nArray[7]
    for i in range(6, -1, -1):
        nArray[i+1]=nArray[i]
    nArray[0] = temp

    return nArray

def left(nArray):
    temp = nArray[0]
    for i in range(1, 8):
        nArray[i-1] = nArray[i]
    nArray[7] = temp

    return nArray

def turn(n, d, array, t):
    if d == 1:
        if t != 1 and n < 4 and array[n-1][2] != array[n][6]:
            turn(n+1, -1, array, -1)
        if t != -1 and n-2 >= 0 and array[n-1][6] != array[n-2][2]:
            turn(n-1, -1, array, 1)
        array[n-1] = right(array[n-1])
    elif d == -1:
        if t != 1 and n <4 and array[n - 1][2] != array[n][6]:
            turn(n + 1, 1, array, -1)
        if t != -1 and n-2 >= 0 and array[n - 1][6] != array[n - 2][2]:
            turn(n - 1, 1, array, 1)
        array[n - 1] = left(array[n - 1])

    return array

array = []
for i in range(4):
    array.append(list(map(int, input())))

k = int(input())
for i in range(k):
    n, d = map(int, input().split())
    array = turn(n, d, array, 0)

result = 0
for i in range(4):
    if array[i][0] == 1:
        result += 2**i

print(result)