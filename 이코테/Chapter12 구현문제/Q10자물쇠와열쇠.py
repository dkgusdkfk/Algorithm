def solution(key, lock):
    answer = True
    #array = [[-1]*3]*3

    for j in range(len(key)):
        #array2 = []
        for r in range(len(key)-1-j, len(key)):
            array2 = []
            for i in range(len(key)):
                array = []
                for k in range(len(key)-1-i,len(key)):
                    array.append(key[r][k])
                #print(array)
                array2.append(array)
            print(array2)





    return answer

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))