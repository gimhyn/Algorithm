N, M = map(int, input().split())
A = list(list(map(int, input().split())) for _ in range(N))
M, K = map(int, input().split())
B = list(list(map(int, input().split())) for _ in range(M))
for r in range(N):
    for c in range(K):
        rc = 0
        for i in range(M):
            rc += A[r][i]*B[i][c]
        print(rc, end=' ')
    print()