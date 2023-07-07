n = int(input())
family = [0 for _ in range(n+1)]
a, b = map(int, input().split())
m = int(input())
for i in range(m):
    x, y = map(int, input().split())
    family[y] = x

def func(k):
    arr = []
    while k != 0:
        arr.append(k)
        k = family[k]
    return arr

def main():
    alist = func(a)
    blist = func(b)
    for i, x in enumerate(alist):
        for j, y in enumerate(blist):
            if x == y:
                print(i+j)
                return
    print(-1)

main()