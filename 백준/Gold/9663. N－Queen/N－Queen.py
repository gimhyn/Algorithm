import sys
input = sys.stdin.readline

def solve(x):
    global ans
    if x == N:
        ans += 1
        return

    for y in range(N):
        if col[y]:
            continue
        elif dia1[x+y]:
            continue
        elif dia2[x-y + N-1]:
            continue

        col[y], dia1[x+y], dia2[x-y + N-1] = 1, 1, 1
        solve(x+1)
        col[y], dia1[x+y], dia2[x-y + N-1] = 0, 0, 0


N = int(input())
col = [0] * N
dia1 = [0] * (2*N)
dia2 = [0] * (2*N)
ans = 0

solve(0)
print(ans)