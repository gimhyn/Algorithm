import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    if round(N**(1/3))**3 == N:
        print(f'#{tc} {round(N**(1/3))}')
    else:
        print(f'#{tc} -1')