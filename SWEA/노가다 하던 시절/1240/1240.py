import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    zro = '0001101'
    one = '0011001'
    two = '0010011'
    thr = '0111101'
    fur = '0100011'
    fiv = '0110001'
    six = '0101111'
    svn = '0111011'
    egh = '0110111'
    nin = '0001011'
    num = [zro, one, two, thr, fur, fiv, six, svn, egh, nin]

    # 시작점 찾기
    password  = []
    flag = 1
    while flag:
        for r in range(N):
            if not flag:
                break
            for c in range(M-6):
                if arr[r][c:c+7] in num and arr[r][c+55] == '1':
                    start = (r, c)
                    flag = 0
                    for i in range(c, c+56, 7):
                        if arr[r][i:i+7] == zro:
                            password.append(0)
                        elif arr[r][i:i+7] == one:
                            password.append(1)
                        elif arr[r][i:i+7] == two:
                            password.append(2)
                        elif arr[r][i:i+7] == thr:
                            password.append(3)
                        elif arr[r][i:i+7] == fur:
                            password.append(4)
                        elif arr[r][i:i+7] == fiv:
                            password.append(5)
                        elif arr[r][i:i+7] == six:
                            password.append(6)
                        elif arr[r][i:i+7] == svn:
                            password.append(7)
                        elif arr[r][i:i+7] == egh:
                            password.append(8)
                        else:
                            password.append(9)

                if not flag:
                    break
    sum = 0
    ans = 0

    for j in range(8):
        ans += password[j]
        if j % 2 == 0:
            sum += password[j]*3
        else:
            sum += password[j]
    if sum % 10 == 0:
        print(f'#{tc} {ans}')
    else:
        print(f'#{tc} 0')
