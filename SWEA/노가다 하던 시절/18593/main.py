import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    ipt= ''
    for _ in range(n):
        ipt += ''.join(input().strip())

    print(f'#{tc}', end=' ')
    for i in range(0, len(ipt), 7):
        bit = int(ipt[i:i+7], 2)
        print(bit, end=' ')
    print()
