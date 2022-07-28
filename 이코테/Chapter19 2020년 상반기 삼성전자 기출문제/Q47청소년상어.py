import sys

info = []
for _ in range(4):
    array = list(map(int, sys.stdin.readline().split()))
    v = []
    for i in range(4):
        v.append(array[2*i : 2*(i+1)])
    info.append(v)

info[0][0][0] = 'shark'
