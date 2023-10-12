from itertools import permutations

n = int(input())
k = int(input())
cards = list(int(input()) for _ in range(n))

result = set()
for card in permutations(cards, k):
    result.add(''.join(list(map(str, list(card)))))

print(len(result))