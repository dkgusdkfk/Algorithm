def cutting(distance):
    flag = 0
    dt = []
    for d in distance:
        temp = []
        array = []
        if d == 0:
            flag = 1
            if array != []:
                dt.append(array)
                array = []
        else:
            if flag == 0:
                temp.append(d)
            else:
                array.append(d)
    if array != []:
        temp += array
    print(dt)

    return dt

def solution(n, weak, dist):
    answer = 0

    distance = []
    wl = len(weak)
    dl = len(dist)
    for i in range(wl-1):
        distance.append(abs(weak[i] - weak[i+1]))
    distance.append((n - weak[wl-1]) + weak[0])
    distance = [distance]

    dt = distance
    while(dt != []):
        distance = dt
        dt = []
        #print(distance)
        for d in distance:
            d[d.index(max(d))] = 0
            for i in cutting(d):
                k = 0
                for j in dist:
                    if j >= sum(i):
                        k = j
                    else:
                        break
                if k != 0:
                    dist.remove(k)
                    d.remove(i)
            if d != []:
                dt.append(d)

    answer = dl - len(dist)
    return answer

weak = [1, 5, 6, 10]
dist = 	[1, 2, 3, 4]
print(solution(12, weak, dist))