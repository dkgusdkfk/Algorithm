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
            if int(i[-1]) >= int(q[-1]):
                if (i[0]==q[0] or q[0]=='-') and (i[1]==q[1] or q[1]=='-') and (i[2]==q[2] or q[2]=='-') and (i[3]==q[3] or q[3]=='-'):
                    count += 1
        answer.append(count)

    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query =["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))