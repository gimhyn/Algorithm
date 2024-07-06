# import sys
# sys.stdin = open('5178_input.txt')

def findv(idx):
    if 2*idx <= N:
        if not arr[2*idx]:
            findv(2*idx)
        if not arr[2*idx+1]:
            findv(2*idx+1)
        arr[idx] = arr[2*idx]+arr[2*idx+1]
        return
    else:
        return


T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = [0]*(N+2)                             #노드 개수 홀수 개여도 함수 돌릴 수 있게
    for _ in range(M):
        i, num = map(int, input().split())
        arr[i] = num

    findv(L)
    print(f'#{tc} {arr[L]}')