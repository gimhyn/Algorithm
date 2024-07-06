import sys
sys.stdin = open('5177_input.txt')

def enq(n):  # -> 우선순위 큐와 힙의 연산 같기에
    global last
    last += 1  # 마지막 노드 추가(완전이진트리 유지)
    h[last] = n  # 마지막 노드에 데이터 삽입
    c = last  # 부모 > 자식 비교를 위해
    p = c // 2  # 부모 번호 계산
    while p >= 1 and h[p] > h[c]:  # 부모가 있고, 부모의 키 값이 더 크면
        h[p], h[c] = h[c], h[p]  # 교환
        c = p
        p = c // 2

def finds(idx):
    if idx//2 >= 1:
        h[idx//2] += h[idx]
        finds(idx//2)
        return
    else:
        return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    h = [0] * (N + 1)
    last = 0  # 힙의 마지막 노드 번호

    lst = list(map(int, input().split()))
    for i in lst:
        enq(i)

    finds(N)
    print(f'#{tc} {h[1]-h[N]}')