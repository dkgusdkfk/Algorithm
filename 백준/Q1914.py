def hanoi(n, s, m, e):
    if n > 0:
        hanoi(n - 1, s, e, m)
        print(s, e)
        hanoi(n - 1, m, s, e)

n = int(input())
print(2 ^ n - 1)
if n <= 20:
    hanoi(n, 1, 2, 3)
