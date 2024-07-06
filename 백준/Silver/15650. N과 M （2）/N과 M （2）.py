import sys
input = sys.stdin.readline

def comb(lev):
    if lev == M:
        # print(path)
        sequence = tuple(sorted(path))
        res.add(sequence)
        return
    for i in range(1, N+1):
        if not used[i]:
            used[i] = 1
            path.append(i)
            comb(lev+1)
            path.pop()
            used[i] = 0


N, M = map(int, input().strip().split())
path = []
used = [0] * (N+1)
res = set()
comb(0)
res = sorted(list(res))
for seq in res:
    print(*seq, end='\n')