def turn(key):
    idx = len(key)-1
    temp = [[-1]*len(key)]*len(key)
    temp = [[1,2,3],[4,5,6],[7,8,9]]
    for i in range(len(key)):
        for j in range(len(key)):
            temp[j][idx-i] = key[i][j]

    return temp

def solution(key, lock):
    answer = False
    l = len(lock) + len(key)*2 -2
    array = [[-1]*l]*l

    start = len(key)-1

    t=0
    while(t<4):
        for i in range(l-len(key)):
            for j in range(l-len(key)):
                arr = [a[:] for a in array]
                for x in range(i,i+len(key)):
                    for y in range(j,j+len(key)):
                        arr[x][y] = key[x-i][y-j]
                flag = 0
                for x in range(start, start+len(lock)):
                    for y in range(start, start+len(lock)):
                        if lock[x-start][y-start] == 1 and arr[x][y] in [-1,0]:
                            continue
                        elif lock[x-start][y-start] == 0 and arr[x][y] == 1:
                            continue
                        else:
                            flag = 1
                            break
                    if flag == 1:
                        break
                if flag == 0:
                    return True
        key = turn(key)
        t += 1

    return answer

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))