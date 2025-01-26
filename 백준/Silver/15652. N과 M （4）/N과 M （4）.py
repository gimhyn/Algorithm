import sys
input = sys.stdin.readline 

N, M = map(int, input().split())

path = []

def perm_repeat(n, m, now):
    if len(path) == m:
        print(*path)
        return
        
    for i in range(now, n+1):
        path.append(i)
        last = i
        perm_repeat(n, m, i)
        path.pop()

perm_repeat(N, M, 1)