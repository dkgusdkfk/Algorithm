import string
import math
def convert_recur(num, base):
    number = string.digits + string.ascii_uppercase
    q, r = divmod(num, base)
    return convert_recur(q, base) + number[r] if q else number[r]

def is_prime(n):
    if n == 1:
        return 0
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return 0
    return 1

def solution(n, k):
    answer = 0

    n = str(convert_recur(n, k))

    n_list = list(n.split('0'))
    for i in n_list:
        if i != '':
            answer += is_prime(int(i))

    return answer

n = 437674
k = 3
print(solution(n,k))