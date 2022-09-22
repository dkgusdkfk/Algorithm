def solution(id_list, report, k):
    answer = []
    id_dict = {key: list([]) for key in id_list}
    id_dict2 = dict.fromkeys(id_list, 0)
    report = list(set(report))

    for rp in report:
        id1, id2 = rp.split()
        id_dict[id2].append(id1)

    for ls in id_dict.values():
        if len(ls) >= k:
            for l in ls:
                id_dict2[l] += 1

    answer = list(id_dict2.values())

    return answer

# id_list = ["muzi", "frodo", "apeach", "neo"]
# report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
# k = 2
id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 2
print(solution(id_list, report, k))