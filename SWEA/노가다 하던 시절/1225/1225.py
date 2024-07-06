import sys
sys.stdin = open('input.txt')
T = 10
for testcase in range(1, T+1):
    tc = int(input())
    pw = list(map(int, input().split()))

    # 암호 배열 모두 한 자리 수 -> 각 수의 최대 차 9


    while calculated > 0:
        for i in range(5):
            calculated = pw[0]-(i+1)
            if calculated <= 0:
                break
            for j in range(7):
                pw[j] = pw[j+1]
            pw[-1] = calculated

    for j in range(7):
        pw[j] = pw[j + 1]
    pw[-1] = 0

    print(f'#{tc}', *pw)