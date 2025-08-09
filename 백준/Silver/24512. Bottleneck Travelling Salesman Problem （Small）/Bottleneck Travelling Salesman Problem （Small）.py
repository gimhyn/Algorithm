import sys
import itertools

input = sys.stdin.readline

N, M = map(int, input().split())

# 인접 행렬 (없으면 None)
graph = [[None] * N for _ in range(N)]
for _ in range(M):
    u, v, c = map(int, input().split())
    graph[u-1][v-1] = c

best_max_cost = float('inf')
best_path = None

# 출발점을 0번(문제에서 1번)으로 고정
vertices = [i for i in range(1, N)]

for perm in itertools.permutations(vertices):
    path = [0] + list(perm)
    valid = True
    max_edge_cost = 0

    # 경로 따라가며 비용 확인
    for i in range(N-1):
        u, v = path[i], path[i+1]
        if graph[u][v] is None:
            valid = False
            break
        max_edge_cost = max(max_edge_cost, graph[u][v])

    # 마지막에서 출발점으로 복귀
    if valid:
        u, v = path[-1], path[0]
        if graph[u][v] is None:
            valid = False
        else:
            max_edge_cost = max(max_edge_cost, graph[u][v])

    # 최적값 갱신
    if valid and max_edge_cost < best_max_cost:
        best_max_cost = max_edge_cost
        best_path = path

if best_path is None:
    print(-1)
else:
    print(best_max_cost)
    print(' '.join(str(x+1) for x in best_path))
