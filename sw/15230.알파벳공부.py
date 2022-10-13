import sys
sys.stdin = open("input.txt", "r")

T = int(input())

alphabet = 'abcdefghijklmnopqrstuvwxyz'

for t in range(1,T+1):
    string = input()

    for i in range(len(string)):
        if string[i] != alphabet[i]:
            i -= 1
            break

    print("#%d %d" % (t, i+1))
