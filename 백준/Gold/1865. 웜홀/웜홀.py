import sys
input = sys.stdin.readline
INF = int(1e9)

tc = int(input())

def bellman_ford():
    dist = [0] * (n + 1)  # 모든 노드가 출발점이 될 수 있도록 초기값을 0으로 설정

    # (n-1)번 반복하며 거리 갱신
    for i in range(n - 1):
        for j in range(len(edges)):
            now, next, cost = edges[j]

            if dist[next] > dist[now] + cost:
                dist[next] = dist[now] + cost

    # 음수 사이클 체크
    for j in range(len(edges)):
        now, next, cost = edges[j]

        if dist[next] > dist[now] + cost:
            print("YES")
            return

    print("NO")

for _ in range(tc):
    n, m, w = map(int, input().strip().split())

    edges = []
    for _ in range(m):
        s, e, t = map(int, input().strip().split())
        edges.append((s, e, t))
        edges.append((e, s, t))  # 도로는 양방향

    for _ in range(w):
        s, e, t = map(int, input().strip().split())
        edges.append((s, e, -t))  # 웜홀은 단방향

    bellman_ford()
