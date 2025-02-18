import sys
input = sys.stdin.readline

INF = int(1e9)

n = int(sys.stdin.readline())  # 노드
m = int(sys.stdin.readline())  # 간선

graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 가는 비용은 0
for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = min(graph[a][b], c)  # 최소 비용으로 저장

for k in range(1, n + 1):  # 경유 노드
    for i in range(1, n + 1):  # 출발 노드
        for j in range(1, n + 1):  # 도착 노드
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]) # 플로이드 뭐시기

# 결과 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        # 갈 수 없는 경우 0 출력
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()
