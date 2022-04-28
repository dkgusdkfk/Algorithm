from itertools import combinations
import sys

sys.stdin = open("sample_input.txt", "r")


def solution(array, n, m, c):
    max1 = 0
    max2 = 0
    max1_row = -1
    max1_array = []
    for row in array:
        for i in range(m):
            # print(max1, max2)
            for col in range(n - m + 1):
                clist = [row[col + k] for k in range(m)]
                for cl in list(combinations(clist, i + 1)):
                    sum = 0
                    total = 0
                    for ck in cl:
                        sum += ck
                        total += ck ** 2
                    if sum <= c:
                        if total > max1:
                            if max1_row == row and len([col + k for k in range(m) if col + k in max1_array]) != 0:
                                max1 = total
                            else:
                                max2 = max1
                                max1 = total
                            max1_row = row
                            max1_array = [col + k for k in range(m)]
                        elif total > max2:
                            if max1_row != row or len([col + k for k in range(m) if col + k in max1_array]) == 0:
                                max2 = total
    return max1 + max2

T = int(input())
for i in range(T):
    n, m, c = map(int, input().split())
    array = []
    for j in range(n):
        array.append(list(map(int, input().split())))

    result = solution(array, n, m, c)
    print("#%d %d" % (i + 1, result))



def solution2(array, n, m, c):
    max1 = 0
    max2 = 0
    max1_row = -1
    max1_array = []
    for row in array:
        for i in range(m):
            for col in range(n - i):
                sum = 0
                total = 0
                for j in range(i + 1):
                    sum += row[col + j]
                    total += row[col + j] * row[col + j]
                if sum <= c:
                    if total > max1:
                        if max1_row == row and len([col + k for k in range(m) if col + k in max1_array]) != 0:
                            max1 = total
                        else:
                            max2 = max1
                            max1 = total
                        max1_row = row
                        max1_array = [col + k for k in range(m)]
                    elif total > max2:
                        if max1_row != row or len([col + k for k in range(m) if col + k in max1_array]) == 0:
                            max2 = total
    return max1 + max2
