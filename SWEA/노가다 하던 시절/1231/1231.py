import sys
sys.stdin = open('input.txt')

T = 10
def inorder(i, n):
    if 2*i <= n:            # 범위 안이라면
        inorder(2*i, n)     # 왼쪽 자식으로 돌리기
    print(arr[i], end='')   # 가장 높은 레벨에 도달하면 프린트
    if 2*i + 1 <= n:        # 오른쪽 자식 노드 있다면
        inorder(2*i+1, n)   # 함수 다시 돌리기


for tc in range(1, T+1):
    N = int(input())
    arr = [0]*(N+1)
    for i in range(N):
        inp = list(input().split())
        p = int(inp[0])
        arr[p] = inp[1]
    # i -> 2i -> 2i+1
    print(f'#{tc}', end=' ')
    inorder(1, N)
    print()