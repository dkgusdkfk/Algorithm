import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    arr, n = input().split()
    array = [int(a) for a in str(arr)]
    print(array)

    #while (n != 0):


