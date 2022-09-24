def solution(n, info):
    answer = []

    a, l = 0, 0

    k = 10
    for i in info[:-1]:
        if i <= 1 and n >= i+1:
            answer.append(i+1)
            l += k
            n -= i+1
        else:
            answer.append(0)
            if i != 0:
                a += k
        k -= 1

    answer.append(n)

    if a >= l:
        answer = [-1]

    return answer

n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]
print(solution(n, info))