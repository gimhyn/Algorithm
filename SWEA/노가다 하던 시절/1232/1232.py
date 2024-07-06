import sys
sys.stdin = open('input.txt')

def order(i):                                       # 후위 연산으로 돌면서
    if arr[i]:
        order(left[i])
        order(right[i])
        if arr[i] == '+':                           # 연산자 만날 때마다 계산값으로 해당 노드 재할당
            arr[i] = arr[left[i]] + arr[right[i]]
        elif arr[i] == '-':
            arr[i] = arr[left[i]] - arr[right[i]]
        elif arr[i] == '*':
            arr[i] = arr[left[i]] * arr[right[i]]
        elif arr[i] == '/':
            arr[i] = arr[left[i]] / arr[right[i]]

T = 10
for tc in range(1, T+1):
    N = int(input())    # 1<= N <= 1000
    left = [0]*(N+1)
    right = [0]*(N+1)
    arr = [0]*(N+1)
    for i in range(N):
        lst = list(input().split())
        idx = int(lst[0])
        if len(lst) > 2:            # 연산자일 경우
            arr[idx] = lst[1]
            left[idx] = int(lst[2])
            right[idx] = int(lst[3])
        else:                       # 숫자일 경우
            arr[idx] = int(lst[1])
    order(1)
    print(f'#{tc} {int(arr[1])}')