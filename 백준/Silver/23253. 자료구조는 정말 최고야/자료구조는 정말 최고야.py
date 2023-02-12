import sys

input = sys.stdin.readline

n, m = map(int, input().split())

result = "Yes"
for i in range(m):
    k = int(input())
    books = list(map(int, input().split()))
    if books != sorted(books, reverse=True):
        result = "No"
        break
print(result)