import sys
input = sys.stdin.readline

n, m = map(int, input().split())
rectangle = [list(map(int, list(input().strip()))) for _ in range(n)]

square = 1

for i in range(n):
    for j in range(m):
        for k in range(min(n - i, m - j), 0, -1):
            if rectangle[i][j] == rectangle[i + k - 1][j] == rectangle[i][j + k - 1] == rectangle[i + k - 1][j + k - 1]:
                square = max(square, k ** 2)
                break

print(square)
