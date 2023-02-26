from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    queue = deque()
    queue.append([begin, 0])
    
    while queue:
        word, cnt = queue.popleft()
        
        if word == target:
            return cnt
        
        for wd in words:
            flag = 0
            for i, w in enumerate(word):
                if wd[i] != w:
                    flag += 1
            if flag == 1:
                queue.append([wd, cnt + 1])
    return 0