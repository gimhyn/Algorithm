# import sys
# sys.stdin = open('4828_input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    max_a = arr[0]
    min_a = arr[0]
    for i in range(len(arr)):
        if arr[i] > max_a:
            max_a = arr[i]
        if arr[i] < min_a:
            min_a = arr[i]

    print(f'#{tc} {max_a - min_a}')