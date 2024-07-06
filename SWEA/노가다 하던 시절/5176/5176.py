import sys
sys.stdin = open('5176_input.txt')
<<<<<<< HEAD
def order(t):
    if t:
        inorder(left[t])
        visited.append(t)   #visited 인덱스 = 저장 값
        inorder(right[t])
=======

def order(t):
    if t:
        order(left[t])
        visited.append(t)   #visited = 방문순서
        order(right[t])
>>>>>>> 4f6ca52028f49db28336a2ae186e7e99b7e10d97

T = int(input())
for tc in range(1, T+1):
    N =int(input())
<<<<<<< HEAD
    arr = [0]*(N+1)
=======
    visited = [0]
>>>>>>> 4f6ca52028f49db28336a2ae186e7e99b7e10d97
    left = [0]*(N+1)
    right = [0]*(N+1)

    for i in range(1, N//2+1):        #완전 이진 트리
        left[i] = 2*i
        if 2*i+1 <= N:
            right[i] = 2*i+1

<<<<<<< HEAD
    inorder(1)
    print(*visited)
    print(f'#{tc} {visited[1]} {visited[N//2]}')

=======
    order(1)
    # print(*visited)
    print(f'#{tc} {visited.index(1)} {visited.index(N//2)}')
>>>>>>> 4f6ca52028f49db28336a2ae186e7e99b7e10d97
