import sys
input = sys.stdin.readline

def dfs(arr, start, leng):
    stack = []
    visited = [0]*(leng + 1)
    stack.append(start)
    visited[start] = 1
    cnt = 1
    while stack:
        now = stack.pop()
        for v in arr[now]:
            if not visited[v]:
                visited[v] = 1
                cnt += 1
                stack.append(v)

    return cnt - 1 #1번 컴퓨터 빼기

N = int(input())
connected = [[] for _ in range(N+1)]
sets = int(input().strip())

for _ in range(sets):
    i, j = map(int, input().split())
    connected[i].append(j)
    connected[j].append(i)

print(dfs(connected, 1, N))
