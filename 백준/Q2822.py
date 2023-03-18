nums = {}
for i in range(1, 9):
    nums[i] = int(input())
nums = sorted(nums.items(), key=lambda item: item[1], reverse=True)

total = 0
result = []
for i in range(5):
    result.append(nums[i][0])
    total += nums[i][1]
result.sort()

print(total)
print(*result)
