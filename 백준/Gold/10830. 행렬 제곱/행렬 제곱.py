import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000)

def matrix_mul(A, B):
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += A[i][k] * B[k][j]
            res[i][j] %= 1000
    return res

def power(A, b):
    if b == 1:
        return [[x % 1000 for x in row]for row in A]
    
    half = power(A, b//2)
    if b % 2 == 0:
        return matrix_mul(half, half)
    else:
        return matrix_mul(matrix_mul(half, half), A)

n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

result = power(matrix, b)

for l in result:
    print(*l)