import sys
sys.stdin = open('4871_input.txt')

def dfs(s, g):
    while True:
        for v in adjl[s]:   # 시작 지점의 인접 노드 중
            if not visited[v]:  # 방문 안 한 노드가 있
                if v == g:
                    return 1

                stack.append(s) # 스택에 원 위치 push
                visited[v] = 1  # 방문 표시
                s = v           # 노드 업데이트
                break
        else:               # 방문 안 한 노드가 없다면
            if stack:
                s = stack.pop() # 스택에서 이전 위치 pop해 되돌아가기
            else:
                return 0    # 더 pop할게 없다면 return 0




T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    # V개 이내의 노드. E개의 간선
    visited = [0] * (V + 1)
    adjl = [[] for _ in range(V+1)]
    stack = []

    for i in range(E):
        start, end = map(int, input().split())
        adjl[start].append(end)

    S, G = map(int, input().split())

    print(f'#{tc} {dfs(S,G)}')






