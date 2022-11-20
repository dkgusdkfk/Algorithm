import sys
sys.stdin = open("input.txt", "r")

T = int(input())

grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for t in range(1, T+1):
    n, k = map(int, input().split())

    students = []
    for i in range(1, n+1):
        score = 0
        m, f, h = map(int, input().split())
        score += 0.35*m + 0.45*f + 0.2*h
        students.append(score)
        if i == k:
            s = score

    students.sort(reverse=True)
    idx = students.index(s)

    result = grade[idx//(n//10)]

    print("#%d %s" % (t, result))