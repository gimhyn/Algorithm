n = int(input())
order = list(map(int, input().split()))
# 학생수 <= 100
ans = []
student = 1
for i in order:
    if i == 0:
        ans.append(student)
    else:
        ans.insert(-i, student)
    student += 1

print(*ans)