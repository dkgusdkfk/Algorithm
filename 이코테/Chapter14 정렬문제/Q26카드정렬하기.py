n = int(input())

card = []
for i in range(n):
    card.append(int(input()))

result = 0
while(len(card)>1):
    card.sort() # 해결 --> 우선순위큐 사용
    a = card.pop(0)
    b = card.pop(0)
    card.append(a+b)
    result += (a+b)

print(result)