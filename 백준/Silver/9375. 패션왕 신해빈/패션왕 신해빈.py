import sys
input = sys.stdin.readline

T = int(input().strip())
for tc in range(T):
    closet = {}
    n = int(input())
    for _ in range(n):
        name, type = input().strip().split()
        if not type in closet:
            closet[type] = [name]
        else:
            closet[type].append(name)

    cnt = 1
    for k in closet:
        cnt *= len(closet[k]) + 1

    print(cnt - 1) # 다 안 입은 경우
