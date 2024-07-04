import sys
input = sys.stdin.readline

def f(n, sr, sc):
    global b_cnt, w_cnt
    clr = paper[sr][sc]
    flag = True
    for r in range(sr, sr+n):
        if not flag:
            break
        for c in range(sc, sc+n):
            if paper[r][c] != clr:
                flag = False
                break
    if flag:
        if clr == 1:
            b_cnt += 1
        else:
            w_cnt += 1

    else:
        n2 = n // 2
        f(n2, sr, sc)
        f(n2, sr+n2, sc)
        f(n2, sr, sc+n2)
        f(n2, sr+n2, sc+n2)




N = int(input().strip())
# 2^1 <= N <= 2^7
paper = list(list(map(int, input().strip().split())) for _ in range(N))
b_cnt = 0
w_cnt = 0
f(N, 0, 0)
print(w_cnt)
print(b_cnt)