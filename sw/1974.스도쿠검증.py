import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    result = 1

    array = []
    for i in range(9):
        arr = list(map(int, input().split()))
        if sorted(arr) != sorted(list(set(arr))):
            result = 0
        array.append(arr)

    for j in range(9):
        a = []
        for i in range(9):
            a.append(array[i][j])
        if sorted(a) != sorted(list(set(a))):
            result = 0
            break

    if result != 0:
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                b = array[i][j:j+3] + array[i+1][j:j+3] + array[i+2][j:j+3]
                if sorted(b) != sorted(list(set(b))):
                    result = 0
                    break
            if result == 0:
                break

    print("#%d %d" % (t, result))

