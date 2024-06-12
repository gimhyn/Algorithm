N, K = list(map(int, input().split()))
d = [i for i in range(1, N+1)]

i = K-1
res = []
while d:
    i %= len(d)
    res.append(d.pop(i))
    i += K-1

ans = '<'+', '.join(str(x) for x in res)+'>'
print(ans)