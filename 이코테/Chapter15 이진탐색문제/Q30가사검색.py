def binary_search(array, target, s, e, start, end):
    count = 0
    while start <= end:
        mid = (start + end) // 2
        if array[mid][s:e] == target[s:e] and len(array[mid]) == len(target):
            count += 1
        elif array[mid][s:e] < target[s:e]:
            start = mid + 1
        else:
            end = mid -1

    return count

def solution(words, queries):
    answer = []

    l = len(words) - 1

    for q in queries:
        s = 0
        e = -1
        idx = q.index('?')
        c = q.count('?')
        if idx == 0:
            s = c+1
        else:
            e = idx
        count = binary_search(words, q, s, e, 0, l)
        answer.append(count)

    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words, queries))