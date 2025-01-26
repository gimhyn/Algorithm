import sys
input = sys.stdin.readline 

N, M = map(int, input().split())

path = []
def perm_repeat(n, m):
    if len(path) == m:
        print(*path)
        return
    for i in range(1, n+1):
        path.append(i)
        perm_repeat(n, m)
        path.pop()

perm_repeat(N, M)