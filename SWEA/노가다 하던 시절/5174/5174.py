import sys
sys.stdin = open('5174_input.txt')

def subtreeN(n):
    global sum
    if child[n]:
        for cn in child[n]:
            subtreeN(cn)
    sum += 1
    return sum

T = int(input())
for tc in range(1, T+1):
    sum = 0
    E, N = map(int, input().split())
    # E개의 간선 개수/ 기준 노드 N
    child = [[] for _ in range(E+2)]           # 해당 노드 번호 인덱스에 자식 노드의 번호가 들어가도록 리스트 생성
    inp = list(map(int, input().split()))
    for i in range(E):
        p, c = inp[2*i], inp[2*i+1]
        child[p].append(c)
    print(f'#{tc} {subtreeN(N)}')
