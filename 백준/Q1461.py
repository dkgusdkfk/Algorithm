n, m = map(int, input().split())
books = sorted(list(map(int, input().split())))

result = 0
if n <= m:
    if books[0] * books[n-1] < 0:
        result += books[0] * 2 + books[n-1] * 2
    else:
        result += max(abs(books[0]), abs(books[n-1])) * 2
else:
    if books[n-1] > 0:
        for i in range(0, n, m):
            result += abs(books[i]) * 2
            if i+m > n:
                break
            if books[i] * books[i+m] < 0:
                break
    if books[0] < 0:
        for j in range(n-1, -1, -m):
            result += abs(books[j]) * 2
            if j-m < 0:
                break
            if books[j] * books[j-m] < 0:
                break

result -= max(abs(books[0]), abs(books[n-1]))

print(result)
