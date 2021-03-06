def possible_seat(seat, x, y, f):
    slist = []
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    for i in range(4):
        if 0 <= x + dx[i] < n and 0 <= y + dy[i] < n:
            if seat[x + dx[i]][y + dy[i]] == f:
                slist.append((x + dx[i], y + dy[i]))
    return slist


n = int(input())

seat = []
for i in range(n):
    seat.append([0] * n)

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
dic = {}
for i in range(n ** 2):
    array = list(map(int, input().split()))
    student = array[0]
    array = array[1:]
    dic[student] = array
    one_list = []
    for s in array:
        for row in range(n):
            for col in range(n):
                if seat[row][col] == s:
                    for i in range(4):
                        if 0 <= row + dx[i] < n and 0 <= col + dy[i] < n:
                            if seat[row + dx[i]][col + dy[i]] == 0:
                                one_list.append((row + dx[i], col + dy[i]))
    one_list.sort()
    if len(one_list) > 1:
        o_count = 0
        for o in one_list:
            if o_count < one_list.count(o):
                max_list = [o]
                o_count = one_list.count(o)
            elif o_count == one_list.count(o):
                max_list.append(o)
        count = -1
        for x, y in max_list:
            if count < len(possible_seat(seat, x, y, 0)):
                count = len(possible_seat(seat, x, y, 0))
                result = (x, y)
    elif len(one_list) == 1:
        result = one_list[0]
    else:
        count = -1
        for i in range(n):
            for j in range(n):
                if seat[i][j] == 0 and count < len(possible_seat(seat, i, j, 0)):
                    count = len(possible_seat(seat, i, j, 0))
                    result = (i, j)

    seat[result[0]][result[1]] = student

sum = 0
for i in range(n):
    for j in range(n):
        c = 0
        for v in dic[seat[i][j]]:
            c += len(possible_seat(seat, i, j, v))
        if c > 0:
            sum += 10 ** (c - 1)

print(sum)
