import sys
sys.stdin = open('5186_input.txt')

T = int(input())
for tc in range(1, T+1):
    n = float(input())
    res = ''
    cnt = 1
    flag = 0
    while cnt <= 12:
        res += str(int(n // (1/2)**cnt))
        j = n //(1/2)**cnt
        k = n % (1/2)**cnt
        if n % (1/2)**cnt == 0:
            flag = 1
            break
        n %= (1/2)**cnt
        cnt += 1

    if flag:
        print(f'#{tc} {res}')
    else:
        print(f'#{tc} overflow')