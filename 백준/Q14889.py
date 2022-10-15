n = int(input())

s = []

def dfs(member, k):
    global answer
    if len(member) == n/2:
        mt = 0
        for i in member:
            for j in member:
                mt += s[i][j]
        other = list(set(range(n)) - set(member))
        ot = 0
        for i in other:
            for j in other:
                ot += s[i][j]
        if abs(mt - ot) < answer:
            answer = abs(mt - ot)
        return

    for i in range(k, n):
        dfs(member + [i], i+1)

for i in range(n):
    score = list(map(int, input().split()))
    s.append(score)

answer = n*100
dfs([], 0)
print(answer)