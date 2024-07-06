import sys
sys.stdin = open('sample_input.txt')

def cuberoot(N):
    start = 1
    end = N
    while True:
        middle = (start + end) // 2
        if middle ** 3 == N:
            return middle
        elif middle ** 3 > N:
            end = middle - 1
        else:
            start = middle + 1
        if start > end:
            return -1
            break

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc} {cuberoot(N)}')