def solution(N, stages):
    dic = {}
    l = len(stages)
    for i in range(1, N+1):
        c = stages.count(i)
        dic[i] = c/l
        l -= c
        # if l==0: 추가 하기

    answer = sorted(dic, key=lambda x: dic[x], reverse=True)

    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))