import sys
sys.stdin = open('5177_input.txt')

def makeh(n):
    global last
    last += 1
    heap[last] = n
    c = last
    p = c // 2
    while p >= 1 and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]  # 교환
        c = p
        p = c // 2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    heap = [0]*(N+1)
    ipt = list(map(int, input().split()))
    last = 0
    for j in ipt:
        makeh(j)

    s = 0
    while N//2 >= 1:
        s += heap[N//2]
        N //= 2
    print(f'#{tc} {s}')