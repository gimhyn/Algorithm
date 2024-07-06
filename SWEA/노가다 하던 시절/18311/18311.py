import sys
sys.stdin = open('input.txt')

V, E = map(int, input().split())
# 정점 개수, 간선 개수
edge_list =[[] for _ in range(V+1)]
lst = list(map(int, input().split()))
check = [0]*(V+1)
for i in range(E):
    edge_list[lst[2*i]].append(lst[2*i+1])
    edge_list[lst[2*i+1]].append(lst[2*i])
print(edge_list)

for lst in edge_list:
    lst.sort()          #sort 쓰지 말라하셨지만...언제 다 정렬합니까.. 이 부분 없어도 우연히 굴러가긴합니다..

stack = []
v = 1
res = []
res.append(v)
stack.append(v)
check[v] = 1
while stack:
    for w in edge_list[v]:

        if check[w] == 0:
            stack.append(v)
            check[w] = 1
            v = w
            res.append(v)
            break
    else:
        v = stack.pop()

print(f'#1', '-'.join(map(str, res)))