n, k = map(int, input().split())

array = list(map(int, input().split()))

robot = [0]*n

step = 0
while(array.count(0) < k):
    temp = array[2 * n - 1]
    for i in range(2*n-1, 0, -1):
        if i < n-1:
            robot[i] = robot[i-1]
        array[i] = array[i-1]
    robot[0] = 0
    array[0] = temp

    for i in range(n-2, -1, -1):
        if robot[i] == 1 and robot[i+1] == 0 and array[i+1] != 0:
            robot[i+1] = 1
            array[i+1] -= 1
            robot[i] = 0
            robot[n-1] = 0

    if array[0] != 0:
        array[0] -= 1
        robot[0] = 1

    step += 1

print(step)