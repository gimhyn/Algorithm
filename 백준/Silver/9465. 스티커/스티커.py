import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    n = int(input())

    if n == 1:
        a = int(input())
        b = int(input())
        print(max(a, b))
        continue

    sticker1 = list(map(int, input().split()))
    sticker2 = list(map(int, input().split()))

    dp1 = [0] * n # 해당 칸을 색칠할 때 최댓값
    dp2 = [0] * n

    dp1[0], dp2[0] = sticker1[0], sticker2[0]

    dp1[1] = dp2[0] + sticker1[1]
    dp2[1] = dp1[0] + sticker2[1]

    for i in range(2, n):
        dp1[i] = max(dp2[i-1], dp1[i-2], dp2[i-2]) + sticker1[i]
        dp2[i] = max(dp1[i-1], dp2[i-2], dp1[i-2]) + sticker2[i]

    print(max(dp1[-1], dp2[-1]))