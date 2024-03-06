# temp = [73, 74, 75, 71, 69, 72, 76, 73]
# answer = []
temp = list(map(int, input().split()))
answer = []
i = 0
while i < len(temp):
    j = i + 1
    while j < len(temp):
        if temp[j] > temp[i]:
            answer.append(j - i)
            break
        j += 1
    if j == len(temp):
        answer.append(0)
    i += 1
# answer.append(0)
print(answer)

# i = 0
# while i < 10:
#     i += 1
#     print(i)
# print(i)
