import sys
sys.stdin = open('input.txt')
#망했어요~~~~~~~~~~~~~~~~!!!!!!!
def findancestor(v1, v2):
    root = 1
    pv = -1
    ancestorv1 = []
    while pv != root:
        pv = parent[v1]
        if pv:
            ancestorv1.append(pv)
            v1 = pv
        else:
            return root
    pv = -1
    while pv != root:
        pv = parent[v2]
        if pv not in ancestorv1:
            v2 = pv
        else:
            return pv
    return root



T = int(input())
for tc in range(1, T+1):
    V, E, c1, c2 = map(int, input().split())
    ipt = list(map(int, input().split()))
    parent = [0]*(V+1)
    child = list([] for _ in range(V+1))
    for i in range(E//2):
        p = ipt[2*i]
        c = ipt[2*i+1]
        child[p].append(c)
        parent[c] = p
    commonancestor = findancestor(c1, c2)

    q = []
    q.append(commonancestor)
    visited = [0]*(V+1)
    cnt = 1
    while q:
        node = q.pop(0)         #디큐
        for j in child[node]:
            if visited[j] == 0:
                cnt += 1
                q.append(j)


    print(f'#{tc} {commonancestor} {cnt}')
