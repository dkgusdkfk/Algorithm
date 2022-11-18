import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    result = -1

    date = input()

    y = date[:4]
    m = date[4:6]
    d = date[6:]

    if int(m) in [1,3,5,7,8,10,12]:
        if 1 <= int(d) <= 31:
            result = y + '/' + m + '/' + d
    elif int(m) in [4,6,9,11]:
        if 1 <= int(d) <= 30:
            result = y + '/' + m + '/' + d
    elif int(m) == 2:
        if 1 <= int(d) <= 28:
            result = y + '/' + m + '/' + d

    print('#%d %s' % (t, result))
