import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    n = int(input())
    o, h, *c = list(map(int, input().split()))