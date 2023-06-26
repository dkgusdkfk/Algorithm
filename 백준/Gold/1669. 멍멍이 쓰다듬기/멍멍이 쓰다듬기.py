import sys
import math

x, y = map(int, sys.stdin.readline().split())
if x == y:
    print(0)
else:
    n = int(math.sqrt(y - x))
    if n ** 2 == y - x:
        print(2 * n - 1)
    else:
        z = (y - x) - n ** 2
        if z <= n:
            print(2 * n)
        else:
            print(2 * n + 1)