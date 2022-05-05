def solution(name):
    answer = 0

    Name = ["A"] * len(name)

    for i in range(len(name)):
        if Name[i] != name[i]:
            answer += min(ord(name[i]) - ord(Name[i]), ord('Z') + 1 - ord(name[i]))

    left = 0
    l = 0
    right = 0
    r = 0
    name = list(name)
    while name in ["A"]:
        while name[0-l] != "A":
            left += 1
            l += 1

        while name[0+r] != "A":
            right += 1
            r += 1

        if left > right:
            answer += right
            Name[0+r] = name[0+r]
        else:
            answer += left
            Name[0-l] = name[0-l]

    return answer


print(solution("JEROEN"))
