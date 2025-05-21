import sys
sys.setrecursionlimit(10**9)

nodes = list(map(int, sys.stdin.read().split()))

def postorder(start, end):
    if start >= end: return
    # mid == end인 경우 처리해줘야

    # 왼쪽 트리 오른쪽 트리 경계 찾기
    mid = end
    for i in range(start+1, end):
        if nodes[start] < nodes[i]:
            mid = i
            break

    # 왼쪽 트리 순회
    postorder(start+1, mid)
    # 오른쪽 트리 순회
    postorder(mid, end)
    print(nodes[start])

postorder(0, len(nodes))