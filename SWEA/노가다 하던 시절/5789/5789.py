import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    n, q = map(int, input().split())
    # n개의 상자, q회의 실행
    # 1 <= n, q <= 10**3
    arr = [0]*(n+1) #초기 상자 세팅

    for i in range(1, q+1):
        l, r = map(int, input().split())
        #i번째 작업에 대해 l부터 r상자까지 값을 i로 변경
        #초기값은 0

        for j in range(l, r+1):
            arr[j] = i

    arr.pop(0)

    print(f'#{tc}', *arr)