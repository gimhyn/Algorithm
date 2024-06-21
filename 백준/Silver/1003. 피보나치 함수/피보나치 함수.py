def f(arr, num):
    if num == 0:
        return arr[num]
    elif num == 1:
        return arr[num]
    else:
        if not arr[num]:
            arr[num] = f(arr, num - 1)+f(arr, num - 2)
        return arr[num]

def fibo(N):
    f(memo_0, N)
    f(memo_1, N)
    return memo_0[N], memo_1[N]


import sys
input = sys.stdin.readline

memo_0 = [1, 0] + [0] * 39
memo_1 = [0, 1] + [0] * 39
T = int(input())
for tc in range(T):
    #  0 <= N <= 40
    n = int(input())
    print(*fibo(n))