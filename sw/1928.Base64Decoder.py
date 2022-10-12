import sys
sys.stdin = open("input.txt", "r")

T = int(input())

arr = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
      'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
      '0','1','2','3','4','5','6','7','8','9','+','/']

for t in range(1, T+1):
    s = list(input())
    value = ''
    for a in s:
        n = arr.index(a)
        bin_n = str(bin(n)[2:])

        while len(bin_n) < 6:
            bin_n = '0' + bin_n
        value += bin_n

    answer = ''
    for i in range(len(s)*6//8):
        data = int(value[i*8: i*8+8], 2)
        answer += chr(data)

    print("#%d %s" % (t, answer))