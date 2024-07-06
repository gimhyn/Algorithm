# import sys
# sys.stdin = open('4835_input.txt')

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    #n = 정수의 개수 #m = 구간의 개수
    # 10 <= n <= 100, 2 <= m < n
    arr = list(map(int, input().split()))

    max_sum = 0
    min_sum = 1000000
    for i in range(n-m+1):
        sum = 0
        for j in range(m):
            sum += arr[i+j]

        if sum > max_sum:
            max_sum = sum
        if sum < min_sum:
            min_sum = sum

    answer = max_sum - min_sum

    print(f'#{tc} {answer}')