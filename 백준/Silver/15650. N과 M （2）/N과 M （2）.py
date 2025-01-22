import sys
input = sys.stdin.readline

N, M = map(int, input().split())

used = [0] * (N+1)
path = []
def orders(n, m, start):
    if len(path) == m:
        print(*path)
        return
    for i in range(start, n+1):
        if not used[i]:
            used[i] = 1
            path.append(i)
            orders(n, m, i)
            path.pop()
            used[i] = 0



orders(N, M, 1)
