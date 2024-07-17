import sys
input = sys.stdin.readline

token = list(input().strip())  # 개행문자 제거
stack = []
num = 0
flag = False  # 플래그 추가
for i in token:
    if i.isdigit():  # 숫자인지 확인
        num = num * 10 + int(i)
    else:
        if flag:  # 플래그가 True이면 음수로 처리
            stack.append(-num)
        else:
            stack.append(num)
        num = 0
        if i == '-':
            flag = True
        elif i == '+':
            continue
if flag:
    stack.append(-num)
else:
    stack.append(num)

res = stack.pop(0)  # 첫번째 숫자를 결과로 설정
for j in stack:
    res += j

print(res)
