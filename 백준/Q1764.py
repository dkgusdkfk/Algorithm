import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = set([input().strip() for _ in range(n)])
b = set([input().strip() for _ in range(m)])

result = sorted(list(a & b))
print(len(result))
for r in result:
    print(r)
