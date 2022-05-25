def solution(s):
    answer = len(s)

    for i in range(1,len(s)//2+1):
        l = 0
        count = 1
        for j in range(0,(len(s)//i)*i,i):
            flag = 1
            for k in range(i):
                if j+i+k < len(s):
                    if s[j+k] != s[j+i+k]:
                        flag = 0
                        break
                else:
                    flag = 0
                    break
            if flag == 1:
                count += 1
            else:
                if count != 1:
                    l += len(str(count)) + i
                    count = 1
                else:
                    l += i
        l += len(s) - len(s)//i*i
        if answer > l:
            answer = l

    return answer

print(solution("abcabcdede"))