n = int(input())

num = list(map(int, input().split()))

# +, -, x, /
op = list(map(int, input().split()))

def dfs(total, k, p, m, mp, d):
    global max_answer, min_answer
    if k == n:
        max_answer = max(total, max_answer)
        min_answer = min(total, min_answer)
        return

    if p:
        dfs(total + num[k], k+1, p-1, m, mp, d)
    if m:
        dfs(total - num[k], k+1, p, m-1, mp, d)
    if mp:
        dfs(total * num[k], k+1, p, m, mp-1, d)
    if d:
        dfs(int(total/num[k]), k+1, p, m, mp, d-1)

max_answer = -1e9
min_answer = 1e9
dfs(num[0], 1, op[0], op[1], op[2], op[3])

print(max_answer)
print(min_answer)