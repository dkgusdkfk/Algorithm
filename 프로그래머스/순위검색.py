def solution(info, query):
    Info = []
    for i in info:
        Info.append(list(i.split()))

    Query = []
    for q in query:
        q = q.replace('and', '')
        Query.append(list(q.split()))

    answer = []
    for q in Query:
        count = 0
        for i in Info:
            flag = 1
            if int(i[-1]) >= int(q[-1]):
                for k in range(4):
                    if i[k] == q[k] or q[k] == '-':
                        continue
                    else:
                        flag = 0
                        break
            else:
                flag = 0
            if flag == 1:
                count += 1
        answer.append(count)

    return answer