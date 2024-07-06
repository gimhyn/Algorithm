N, M, V = map(int, input().split())
#정점 N <= 1,000 간선 M<= 10,000, V:시작점
adjl = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    if b not in adjl[a]:
        adjl[a].append(b)
        adjl[b].append(a)
    # 간선 양방향 & 여러개 존재 가능
#번호 작은 정점부터 탐색!
for vertex in adjl:
    vertex.sort()
visited = [0]*(N+1)

#DFS
v = V           # 시작점 설정
visited[v] = 1     # 시작점 방문 처리
stack = []
print(v, end=' ')

while True:
    for w in adjl[v]:
        if visited[w] == 0:
            stack.append(v)
            visited[w] = 1
            print(w, end=' ')
            v = w
            break
    else:
        if stack:
           v = stack.pop()
        else:
            break

print( )

#BFS
from collections import deque

visited = [0]*(N+1)
v = V
visited[v] = 1
queue = deque()
queue.append(v)
print(v, end=' ')
while queue:
    v = queue.popleft()
    for w in adjl[v]:
        if visited[w] == 0:
            visited[w] = 1
            queue.append(w)
            print(w, end=' ')


