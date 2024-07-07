import sys
input = sys.stdin.readline

def perm(n, num, path, idx):
    if len(path) == num:
        print(*path)
        return

    for i in range(idx, n+1):
        perm(n, num, path+[i], i)




N, M = map(int, input().strip().split())

perm(N, M, [], 1)