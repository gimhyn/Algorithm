target = int(input())
max_cnt = 0
lst = []

for num in range(target//2, target+1):
    cnt = 2
    lst.append(target)
    lst.append(num)
    a = target
    b = num
    while a - b >= 0:
        lst.append(a - b)
        a = lst[-2]
        b = lst[-1]
        cnt += 1
    if max_cnt < cnt:
        max_cnt = cnt
        lst = lst[-max_cnt:]    #리스트 앞 비워주기

print(max_cnt)
print(*lst[:max_cnt])