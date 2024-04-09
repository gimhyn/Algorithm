def f(i, target, s):
    global ans
    if ans < s:
        return
    if i == n:
        if target <= s < ans:
            ans = s
        return
    f(i+1, target, s + h_list[i])
    f(i+1, target, s)


T = int(input())
for tc in range(1, T+1):
    n, b = map(int, input().split())
    h_list = list(map(int, input().split()))
    ans = float('inf')

    f(0, b, 0)
    print(f'#{tc} {ans-b}')