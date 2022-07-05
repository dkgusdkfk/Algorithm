# 학생수 n
n = int(input())

# 학생 정보
info = []
for i in range(n):
   info.append(input().split())

info.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in info:
    print(i[0])

# 학생 정보
# info = []
# for i in range(n):
#     name, korean, english, math = input().split()
#     info.append([name, int(korean), int(english), int(math)])
#
# for i in range(1, len(info)):
#     for j in range(i,0,-1):
#         if info[j][1] > info[j-1][1]:
#             info[j], info[j-1] = info[j-1], info[j]
#         elif info[j][1] == info[j-1][1]:
#             if info[j][2] < info[j-1][2]:
#                 info[j], info[j-1] = info[j-1], info[j]
#             elif info[j][2] == info[j-1][2]:
#                 if info[j][3] > info[j - 1][3]:
#                     info[j], info[j - 1] = info[j - 1], info[j]
#                 elif info[j][3] == info[j - 1][3]:
#                     if info[j][0] < info[j-1][0]:
#                         info[j], info[j - 1] = info[j - 1], info[j]