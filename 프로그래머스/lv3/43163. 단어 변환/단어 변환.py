answer = 1e9
def solution(begin, target, words):
    isSelected = [False] * len(words)
    sol(begin, target, words, isSelected, 0)
    if answer == 1e9:
        return 0
    return answer


def sol(begin, target, words, isSelected, cnt):
    global answer
    if begin == target:
        answer = min(answer, cnt)
        return
    for i, w in enumerate(words):
        if isSelected[i]: continue
        if check(begin, w):
            isSelected[i] = True
            sol(w, target, words, isSelected, cnt + 1)
            isSelected[i] = False
    return 0

def check(w1, w2):
    flag = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            flag += 1
        if flag == 2:
            return False
    return True