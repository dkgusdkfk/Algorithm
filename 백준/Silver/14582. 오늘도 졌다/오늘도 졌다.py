arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

sum1 = 0
sum2 = 0
result = 'No'
for a, b in zip(arr1, arr2):
    sum1 += a
    if sum1 > sum2:
        result = 'Yes'
    sum2 += b

print(result)