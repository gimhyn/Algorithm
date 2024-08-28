import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().strip().split())

def bfs():
    if N >= K:
        return N - K
    
    q = deque()
    q.append((N, 0))  # (location, time)
    visited = [0] * 100001
    visited[N] = 1
    
    while q:
        location, time = q.popleft()
        
        for nl in (location * 2, location - 1, location + 1):
            if nl == K:
                return time + 1
            if 0 <= nl < 100001 and not visited[nl]:
                visited[nl] = 1
                q.append((nl, time + 1))

print(bfs())
