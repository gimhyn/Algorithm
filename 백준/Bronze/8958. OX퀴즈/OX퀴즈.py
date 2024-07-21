import sys

input = sys.stdin.readline

T = int(input())
for tc in range(T):
    arr = input()
    cnt = 0
    res = 0
    for i in arr:
        if i == 'O':
            cnt += 1
            res += cnt
        else:
            cnt = 0
    print(res)