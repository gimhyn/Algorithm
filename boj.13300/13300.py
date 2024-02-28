N, K = map(int, input().split())
# 학생 수  1<= N <= 1000, 1<K<=1,000
students = []
for i in range(N):
    s, y = map(int, input().split())
    students.append([s, y])

sum = 0
girl=[0]*7
boy=[0]*7
for student in students:
    if student[0] == 0:     # 여학생
        girl[student[1]] += 1
    else:
        boy[student[1]] += 1

for i in range(1, 7):
    if girl[i] % K != 0:
        sum += girl[i] // K + 1
    elif girl[i] % K == 0:
        sum += girl[i] // K
    if boy[i] % K != 0:
        sum += boy[i] // K + 1
    elif boy[i] % K == 0:
        sum += boy[i] // K

print(sum)


