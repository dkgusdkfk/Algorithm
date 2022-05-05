from itertools import combinations

def solution(relation):
    answer = 0

    r = [i for i in range(len(relation[0]))]
    for i in range(1, len(relation)+1):
        comb = combinations(r, i)
        for c in comb:
            array = [tuple([rt[c_value] for c_value in c]) for rt in relation]
            if len(set(array)) == len(relation):
                for c_value in c:
                    r.remove(c_value)
                answer += 1

    return answer

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))