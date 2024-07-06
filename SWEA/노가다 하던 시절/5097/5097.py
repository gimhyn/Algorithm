# import sys
# sys.stdin = open('5097_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 수열 길이 = N, 작업 M번
    turn = M % N
    lst = input().split()
    print(f'#{tc} {lst[turn]}')
