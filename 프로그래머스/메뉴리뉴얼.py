from itertools import combinations

def solution(orders, course):
    answer = []

    o_count = []
    for o in orders:
        o_count.append(len(o))
    menu = []
    for c in course:
        for o in orders:
            o = list(o)
            o.sort()
            menu += list(combinations(o, c))

    menu.sort()
    pre = ()
    a = []
    for m in menu:
        if m == pre:
            continue
        if menu.count(m) >= 2:
            pre = m
            a.append(("".join(m), menu.count(m)))

    max = [[('', 0)] for _ in range(len(course))]

    idx = 0
    for c in course:
        for v in a:
            if len(v[0]) == c:
                if v[1] > max[idx][0][1]:
                    max[idx] = [v]
                elif v[1] == max[idx][0][1]:
                    max[idx].append(v)
        idx += 1

    for m in max:
        for n in range(len(m)):
            answer.append(m[n][0])

    answer.sort()
    while '' in answer:
        answer.remove('')
    return answer

print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))