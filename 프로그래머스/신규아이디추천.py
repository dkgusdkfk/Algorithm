def solution(new_id):
    answer = ''

    # 1
    new_id = new_id.lower()

    # 2
    for v in new_id:
        if not(v.islower() or '0'<=v<='9' or v in ['-','_','.']):
            new_id = new_id.replace(v,"")

    # 3
    count = 0
    for v in new_id:
        if v == '.':
            if count == 0:
                count += 1
                answer += v
        else:
            count = 0
            answer += v

    # 4
    if answer[0] == '.':
        answer = answer[1:]
    if len(answer) > 0:
        if answer[-1] == '.':
            answer = answer[:-1]

    # 5
    if answer == "":
        answer = "a"

    # 6
    if len(answer) >= 16:
        answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]

    # 7
    if len(answer) <= 2:
        while(len(answer)<3):
            answer = answer + answer[-1]

    return answer

new_id = input()
result = solution(new_id)

print(result)